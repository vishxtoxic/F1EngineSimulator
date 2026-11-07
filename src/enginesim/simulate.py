"""Simulation declarations; internal units are SI: m, s, kg, N, W, and rad/s."""

from collections.abc import Callable

import numpy as np

from .engine import Engine
from .environment import Environment
from .vehicle import Vehicle


def evaluate_forces(
    state: np.ndarray, engine: Engine, vehicle: Vehicle, environment: Environment
) -> np.ndarray:
    """Evaluate forces for a state containing SI quantities; return force values in N."""
    raise NotImplementedError("TODO")


def derivative(
    t: float, state: np.ndarray, engine: Engine, vehicle: Vehicle, environment: Environment
) -> np.ndarray:
    """Evaluate the state derivative at time t in s; return SI state rates."""
    raise NotImplementedError("TODO")


def stop_at_time(t: float, state: np.ndarray, limit_s: float) -> bool:
    """Check time t in s against a time limit in s; return whether to stop."""
    raise NotImplementedError("TODO")


def stop_at_speed(t: float, state: np.ndarray, limit_ms: float) -> bool:
    """Check state speed in m/s against a limit in m/s; return whether to stop."""
    raise NotImplementedError("TODO")


def stop_at_distance(t: float, state: np.ndarray, limit_m: float) -> bool:
    """Check state distance in m against a limit in m; return whether to stop."""
    raise NotImplementedError("TODO")


def simulate_run(
    engine: Engine,
    vehicle: Vehicle,
    environment: Environment,
    derivative_fn: Callable[..., np.ndarray],
) -> "Result":
    """Run a simulation from the supplied model objects; return a Result."""
    raise NotImplementedError("TODO")
