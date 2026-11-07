"""Analysis declarations; internal units are SI: m, s, kg, N, W, and rad/s."""

import numpy as np

from .engine import Engine
from .environment import Environment
from .results import Result
from .vehicle import Vehicle


def equilibrium_top_speed(
    engine: Engine, vehicle: Vehicle, environment: Environment
) -> float:
    """Find equilibrium top speed for the model; return speed in m/s."""
    raise NotImplementedError("TODO")


def convergence_study(
    engine: Engine,
    vehicle: Vehicle,
    environment: Environment,
    time_steps_s: np.ndarray,
) -> np.ndarray:
    """Study time-step convergence in s; return convergence results."""
    raise NotImplementedError("TODO")


def energy_check(result: Result, vehicle: Vehicle) -> float:
    """Check result energy for a vehicle; return energy discrepancy in J."""
    raise NotImplementedError("TODO")
