"""Unit conversion declarations; internal units are SI: m, s, kg, N, W, and rad/s."""

import math

GRAVITY: float = 9.81  # m/s^2
AIR_SPECIFIC_GAS_CONSTANT: float = 287.058  # J/(kg*K)
SEA_LEVEL_DENSITY: float = 1.225 #kg/m^3


def rpm_to_rad_s(rpm: float) -> float:
    """Convert rotational speed from rpm to rad/s; return the speed in rad/s."""
    return rpm * 2 * math.pi / 60


def rad_s_to_rpm(rad_s: float) -> float:
    """Convert rotational speed from rad/s to rpm; return the speed in rpm."""
    return rad_s * 60 / (2 * math.pi)


def kmh_to_ms(speed_kmh: float) -> float:
    """Convert speed from km/h to m/s; return the speed in m/s."""
    return speed_kmh * 1000 / 3600


def ms_to_kmh(speed_ms: float) -> float:
    """Convert speed from m/s to km/h; return the speed in km/h."""
    return speed_ms * 3600 / 1000
