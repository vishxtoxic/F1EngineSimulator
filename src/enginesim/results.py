"""Simulation result declarations; internal units are SI: m, s, kg, N, W, and rad/s."""

from dataclasses import dataclass

import numpy as np


@dataclass
class Result:
    """Store simulation histories in SI units."""

    t: np.ndarray
    v: np.ndarray
    x: np.ndarray
    gear: np.ndarray
    rpm: np.ndarray

    def time_to_speed(self, speed_ms: float) -> float:
        """Find time to speed in m/s; return time in s."""
        raise NotImplementedError("TODO")

    def speed_at_time(self, time_s: float) -> float:
        """Find speed at time in s; return speed in m/s."""
        raise NotImplementedError("TODO")

    def distance_at_time(self, time_s: float) -> float:
        """Find distance at time in s; return distance in m."""
        raise NotImplementedError("TODO")

    def top_speed(self) -> float:
        """Find maximum recorded speed; return speed in m/s."""
        raise NotImplementedError("TODO")

    def shift_points(self) -> np.ndarray:
        """Find gear shift points; return shift times in s."""
        raise NotImplementedError("TODO")
