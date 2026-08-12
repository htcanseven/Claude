"""Models: WDCNN-style baseline and the proposed compositional network."""
from __future__ import annotations

import torch
import torch.nn as nn
from torch.autograd import Function


class CNN1D(nn.Module):
    """WDCNN-style: wide first kernel, then stacked small-kernel conv blocks.

    Input: (batch, n_channels, win) raw (per-channel standardized) signal.
    """

    def __init__(self, n_channels: int, n_classes: int, width: int = 16):
        super().__init__()
        w = width
        self.features = nn.Sequential(
            nn.Conv1d(n_channels, w, kernel_size=64, stride=8, padding=28),
            nn.BatchNorm1d(w), nn.ReLU(), nn.MaxPool1d(2),
            nn.Conv1d(w, 2 * w, 3, padding=1),
            nn.BatchNorm1d(2 * w), nn.ReLU(), nn.MaxPool1d(2),
            nn.Conv1d(2 * w, 4 * w, 3, padding=1),
            nn.BatchNorm1d(4 * w), nn.ReLU(), nn.MaxPool1d(2),
            nn.Conv1d(4 * w, 4 * w, 3, padding=1),
            nn.BatchNorm1d(4 * w), nn.ReLU(),
            nn.AdaptiveAvgPool1d(1),
        )
        self.head = nn.Sequential(
            nn.Flatten(),
            nn.Dropout(0.3),
            nn.Linear(4 * w, n_classes),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.head(self.features(x))


# --- proposed method ----------------------------------------------------

class _GradReverse(Function):
    @staticmethod
    def forward(ctx, x, lambd):
        ctx.lambd = lambd
        return x.view_as(x)

    @staticmethod
    def backward(ctx, grad):
        return -ctx.lambd * grad, None


def grad_reverse(x: torch.Tensor, lambd: float = 1.0) -> torch.Tensor:
    """Gradient-reversal: the layer below is trained to *defeat* the head above."""
    return _GradReverse.apply(x, lambd)


class _Encoder(nn.Module):
    """Per-modality 1D conv encoder (wide first kernel, then small kernels)."""

    def __init__(self, n_channels: int, width: int = 16, out_dim: int = 128):
        super().__init__()
        w = width
        self.net = nn.Sequential(
            nn.Conv1d(n_channels, w, kernel_size=64, stride=8, padding=28),
            nn.BatchNorm1d(w), nn.ReLU(), nn.MaxPool1d(2),
            nn.Conv1d(w, 2 * w, 3, padding=1),
            nn.BatchNorm1d(2 * w), nn.ReLU(), nn.MaxPool1d(2),
            nn.Conv1d(2 * w, 4 * w, 3, padding=1),
            nn.BatchNorm1d(4 * w), nn.ReLU(), nn.MaxPool1d(2),
            nn.Conv1d(4 * w, 4 * w, 3, padding=1),
            nn.BatchNorm1d(4 * w), nn.ReLU(),
            nn.AdaptiveAvgPool1d(1),
            nn.Flatten(),
        )
        self.proj = nn.Sequential(nn.Linear(4 * w, out_dim), nn.ReLU())

    def forward(self, x):
        return self.proj(self.net(x))


class CompositionalNet(nn.Module):
    """Multimodal, condition-invariant, compositional fault diagnosis.

    Three design choices, each answering a specific property of this dataset:

    1. *Separate vibration and current encoders with a learned cross-modal
       gate.* Vibration responds to mechanical defects and current to
       electromagnetic ones, so a mechanical-electrical compound fault needs
       both; the gate lets the network weight each modality per sample instead
       of committing to one fusion ratio.
    2. *Multi-label component head.* A compound fault is represented as the
       union of its single-fault components rather than as its own class, so
       combinations never seen in training remain expressible at test time.
    3. *Adversarial condition head behind a gradient-reversal layer.* Speed and
       load are recoverable from the signal and otherwise dominate the
       embedding; training the trunk to defeat a condition predictor pushes it
       toward representations that transfer to unseen operating conditions.

    Optional ``n_extra`` appends precomputed physics features (envelope-order
    band energies) to the fused embedding — order-domain features are
    speed-invariant by construction and complement the learned ones.
    """

    def __init__(self, n_vib: int, n_cur: int, n_components: int,
                 n_conditions: int, width: int = 16, emb_dim: int = 128,
                 n_extra: int = 0):
        super().__init__()
        self.vib = _Encoder(n_vib, width, emb_dim)
        self.cur = _Encoder(n_cur, width, emb_dim)
        self.gate = nn.Sequential(
            nn.Linear(2 * emb_dim, emb_dim), nn.Sigmoid())
        fused_dim = emb_dim + n_extra
        self.trunk = nn.Sequential(
            nn.Linear(fused_dim, emb_dim), nn.ReLU(), nn.Dropout(0.3))
        self.component_head = nn.Linear(emb_dim, n_components)
        self.condition_head = nn.Sequential(
            nn.Linear(emb_dim, 64), nn.ReLU(), nn.Linear(64, n_conditions))

    def embed(self, x_vib, x_cur, extra=None):
        hv, hc = self.vib(x_vib), self.cur(x_cur)
        g = self.gate(torch.cat([hv, hc], dim=1))
        fused = g * hv + (1.0 - g) * hc
        if extra is not None:
            fused = torch.cat([fused, extra], dim=1)
        return self.trunk(fused), g

    def forward(self, x_vib, x_cur, extra=None, lambd: float = 0.0):
        z, gate = self.embed(x_vib, x_cur, extra)
        comp_logits = self.component_head(z)
        cond_logits = self.condition_head(grad_reverse(z, lambd))
        return comp_logits, cond_logits, z, gate
