"""Unit conversion declarations; internal units are SI: m, s, kg, N, W, and rad/s."""

GRAVITY: float | None = None  # TODO
AIR_SPECIFIC_GAS_CONSTANT: float | None = None  # TODO
SEA_LEVEL_DENSITY: float | None = None  # TODO


def rpm_to_rad_s(rpm: float) -> float:
    """Convert rotational speed from rpm to rad/s; return the speed in rad/s."""
    raise NotImplementedError("TODO")


def rad_s_to_rpm(rad_s: float) -> float:
    """Convert rotational speed from rad/s to rpm; return the speed in rpm."""
    raise NotImplementedError("TODO")


def kmh_to_ms(speed_kmh: float) -> float:
    """Convert speed from km/h to m/s; return the speed in m/s."""
    raise NotImplementedError("TODO")


def ms_to_kmh(speed_ms: float) -> float:
    """Convert speed from m/s to km/h; return the speed in km/h."""
    raise NotImplementedError("TODO")
