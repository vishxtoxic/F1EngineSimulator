"""Environment declarations; internal units are SI: m, s, kg, N, W, and rad/s."""

from dataclasses import dataclass


@dataclass
class Environment:
    """Describe ambient conditions using SI units."""

    temperature_k: float
    pressure_pa: float
    headwind_ms: float
    slope_rad: float


def air_density(temperature_k: float, pressure_pa: float) -> float:
    """Calculate air density from temperature in K and pressure in Pa; return density in kg/m^3."""
    raise NotImplementedError("TODO")
