"""Powertrain declarations; internal units are SI: m, s, kg, N, W, and rad/s."""

import numpy as np

from .engine import Engine
from .vehicle import Vehicle


def engine_rpm(speed_ms: float, wheel_radius_m: float, ratio: float) -> float:
    """Calculate engine speed from vehicle speed in m/s, radius in m, and ratio; return rpm."""
    raise NotImplementedError("TODO")


def wheel_force(
    engine: Engine, vehicle: Vehicle, speed_ms: float, gear: int
) -> float:
    """Calculate wheel force at speed in m/s and gear; return force in N."""
    raise NotImplementedError("TODO")


def gear_options(vehicle: Vehicle, speed_ms: float, engine: Engine) -> np.ndarray:
    """Return available gears at speed in m/s; return gear indices as an array."""
    raise NotImplementedError("TODO")


def select_gear(vehicle: Vehicle, engine: Engine, speed_ms: float) -> int:
    """Select a gear at speed in m/s; return the selected gear index."""
    raise NotImplementedError("TODO")
