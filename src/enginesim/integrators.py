"""Integration declarations; internal units are SI: m, s, kg, N, W, and rad/s."""

from collections.abc import Callable

import numpy as np


def euler_step(
    state: np.ndarray, derivative_fn: Callable[..., np.ndarray], t: float, dt: float
) -> np.ndarray:
    """Advance state at time t by dt seconds with a derivative function; return new state."""
    raise NotImplementedError("TODO")


def rk4_step(
    state: np.ndarray, derivative_fn: Callable[..., np.ndarray], t: float, dt: float
) -> np.ndarray:
    """Advance state at time t by dt seconds with RK4; return the new state."""
    raise NotImplementedError("TODO")
