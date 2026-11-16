"""Environment declarations; internal units are SI: m, s, kg, N, W, and rad/s."""

from dataclasses import dataclass

from .units import AIR_SPECIFIC_GAS_CONSTANT


@dataclass
class Environment:
    """Describe ambient conditions using SI units."""

    temperature_k: float
    pressure_pa: float
    headwind_ms: float
    slope_rad: float


def air_density(temperature_k: float, pressure_pa: float) -> float:
    """Calculate air density from temperature in K and pressure in Pa; return density in kg/m^3."""
    if temperature_k <= 0:
        raise ValueError("temperature_k must be positive")
    if pressure_pa <= 0:
        raise ValueError("pressure_pa must be positive")
    return pressure_pa / (AIR_SPECIFIC_GAS_CONSTANT * temperature_k)
