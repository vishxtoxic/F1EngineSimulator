"""Integration declarations; internal units are SI: m, s, kg, N, W, and rad/s."""

from collections.abc import Callable

import numpy as np


def euler_step(
    state: np.ndarray, derivative_fn: Callable[..., np.ndarray], t: float, dt: float
) -> np.ndarray:
    """Advance state at time t by dt seconds with a derivative function; return new state."""
    state = np.asarray(state, dtype=float)
    return state + dt * np.asarray(derivative_fn(t, state), dtype=float)


def rk4_step(
    state: np.ndarray, derivative_fn: Callable[..., np.ndarray], t: float, dt: float
) -> np.ndarray:
    """Advance state at time t by dt seconds with RK4; return the new state."""
    state = np.asarray(state, dtype=float)
    k1 = np.asarray(derivative_fn(t, state), dtype=float)
    k2 = np.asarray(derivative_fn(t + dt / 2, state + dt * k1 / 2), dtype=float)
    k3 = np.asarray(derivative_fn(t + dt / 2, state + dt * k2 / 2), dtype=float)
    k4 = np.asarray(derivative_fn(t + dt, state + dt * k3), dtype=float)
    return state + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6
