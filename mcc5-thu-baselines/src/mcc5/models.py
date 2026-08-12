"""Baseline neural models. First pass: a compact WDCNN-style 1D CNN."""
from __future__ import annotations

import torch
import torch.nn as nn


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
