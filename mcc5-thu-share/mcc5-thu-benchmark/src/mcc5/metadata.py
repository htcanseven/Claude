"""Parse MCC5-THU motor filenames into structured labels.

Naming convention (dataset paper, Table 5), e.g.:

    Bearing_inner_L_speed_circulation_20Nm_1000rpm.csv
    Winding_H_and_bearing_outer_H_torque_circulation_40Nm_3000rpm.csv

i.e. ``<fault_desc>_<speed|torque>_circulation_<T>Nm_<S>rpm`` where
``fault_desc`` may join two single faults with ``_and_`` (compound faults).

``speed_circulation``  = constant torque, speed follows the 0->S rpm profile.
``torque_circulation`` = constant speed, torque follows the 0->T Nm profile.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field, asdict
from pathlib import Path

_PATTERN = re.compile(
    r"^(?P<fault>.+?)_(?P<profile>speed|torque)_?circulation"
    r"_(?P<torque>\d+(?:\.\d+)?)\s*Nm"
    r"_(?P<speed>\d+)\s*rpm"
    r"(?:_(?P<acq>\d{12}))?",
    re.IGNORECASE,
)

# Families used to repair abbreviated compound components: in
# ``bearing_outer_H_and_inner_H`` the second part is written as ``inner_H``
# and must inherit the ``bearing`` family from the first part.
_FAMILIES = ("bearing", "winding", "static_eccentricity",
             "dynamic_eccentricity", "voltage_unbalance", "broken_bar")

_BEARING_PARTS = ("inner", "outer", "ball")


def _normalize_components(parts: list[str]) -> list[str]:
    """Give every component its explicit family prefix."""
    out: list[str] = []
    for p in parts:
        if not p.startswith(_FAMILIES) and p.startswith(_BEARING_PARTS):
            p = f"bearing_{p}"
        out.append(p)
    return out


@dataclass
class RunInfo:
    file: str
    fault_full: str          # normalized 24-class label
    components: list[str] = field(default_factory=list)  # multi-label parts
    is_compound: bool = False
    profile: str = ""        # speed_circulation | torque_circulation
    torque_nm: float = 0.0
    speed_rpm: int = 0
    condition: str = ""      # operating-condition group id
    acq: str = ""            # acquisition stamp YYMMDDHHMMSS from the filename

    def to_dict(self) -> dict:
        d = asdict(self)
        d["components"] = "+".join(self.components)
        return d


def parse_filename(path: str | Path) -> RunInfo:
    stem = Path(path).stem.strip()
    m = _PATTERN.match(stem)
    if not m:
        raise ValueError(f"unrecognized filename: {stem!r}")
    fault = m.group("fault").strip("_").lower()
    profile = f"{m.group('profile').lower()}_circulation"
    torque = float(m.group("torque"))
    speed = int(m.group("speed"))
    components = _normalize_components(
        [c.strip("_") for c in fault.split("_and_")])
    return RunInfo(
        file=str(path),
        fault_full=fault,
        components=components,
        is_compound=len(components) > 1,
        profile=profile,
        torque_nm=torque,
        speed_rpm=speed,
        condition=f"{profile}_{torque:g}Nm_{speed}rpm",
        acq=m.group("acq") or "",
    )
