"""Longitudinal physics declarations; internal units are SI: m, s, kg, N, W, and rad/s."""


def air_relative_speed(speed_ms: float, headwind_ms: float) -> float:
    """Calculate relative air speed from vehicle and headwind speeds in m/s; return m/s."""
    raise NotImplementedError("TODO")


def drag_force(cd_a_m2: float, air_speed_ms: float, air_density_kg_m3: float) -> float:
    """Calculate drag from area in m^2, speed in m/s, and density in kg/m^3; return N."""
    raise NotImplementedError("TODO")


def rolling_force(mass_kg: float, rolling_coeff: float) -> float:
    """Calculate rolling force from mass in kg and coefficient; return force in N."""
    raise NotImplementedError("TODO")


def gradient_force(mass_kg: float, slope_rad: float) -> float:
    """Calculate gradient force from mass in kg and slope in rad; return force in N."""
    raise NotImplementedError("TODO")


def max_traction_force(
    mass_kg: float, friction_coeff: float, driven_weight_fraction: float
) -> float:
    """Calculate maximum traction from mass in kg, coefficient, and fraction; return N."""
    raise NotImplementedError("TODO")


def net_force(
    drive_force_n: float,
    drag_force_n: float,
    rolling_force_n: float,
    gradient_force_n: float,
) -> float:
    """Calculate net force from component forces in N; return net force in N."""
    raise NotImplementedError("TODO")
