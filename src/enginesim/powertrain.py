"""Powertrain declarations; internal units are SI: m, s, kg, N, W, and rad/s."""

import numpy as np
from typing import overload

from .engine import Engine
from .vehicle import Vehicle


@overload
def engine_rpm(speed_ms: float, wheel_radius_m: float, ratio: float) -> float:
    ...


@overload
def engine_rpm(speed_ms: float, wheel_radius_m: float, ratio: np.ndarray) -> np.ndarray:
    ...


def engine_rpm(
    speed_ms: float, wheel_radius_m: float, ratio: float | np.ndarray
) -> float | np.ndarray:
    """Calculate engine speed from vehicle speed in m/s, radius in m, and ratio; return rpm."""
    if wheel_radius_m <= 0:
        raise ValueError("wheel_radius_m must be positive")
    if np.any(np.asarray(ratio) < 0):
        raise ValueError("ratio must be non-negative")
    return speed_ms / (2 * np.pi * wheel_radius_m) * ratio * 60


def wheel_force(
    engine: Engine, vehicle: Vehicle, speed_ms: float, gear: int
) -> float:
    """Calculate wheel force at speed in m/s and gear; return force in N."""
    if gear < 0 or gear >= len(vehicle.overall_ratios):
        raise IndexError("gear index is out of range")
    ratio = float(vehicle.overall_ratios[gear])
    rpm = max(
        engine_rpm(speed_ms, vehicle.wheel_radius_m, ratio),
        vehicle.launch_rpm,
    )
    return engine.torque(rpm) * ratio * vehicle.driveline_efficiency / vehicle.wheel_radius_m


def gear_options(vehicle: Vehicle, speed_ms: float, engine: Engine) -> np.ndarray:
    """Return available gears at speed in m/s; return gear indices as an array."""
    if vehicle.wheel_radius_m <= 0:
        raise ValueError("wheel_radius_m must be positive")
    ratios = np.asarray(vehicle.overall_ratios, dtype=float)
    rpms = engine_rpm(speed_ms, vehicle.wheel_radius_m, ratios)
    return np.flatnonzero(rpms <= engine.rpm_max)


def select_gear(vehicle: Vehicle, engine: Engine, speed_ms: float) -> int:
    """Select a gear at speed in m/s; return the selected gear index."""
    options = gear_options(vehicle, speed_ms, engine)
    if options.size == 0:
        raise ValueError("no gear is available at this speed")
    forces = np.array([wheel_force(engine, vehicle, speed_ms, int(gear)) for gear in options])
    return int(options[np.argmax(forces)])
