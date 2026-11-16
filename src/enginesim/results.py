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
        reached = np.flatnonzero(self.v >= speed_ms)
        if reached.size == 0:
            raise ValueError("speed was not reached during the simulation")
        index = int(reached[0])
        if index == 0:
            return float(self.t[0])
        return float(np.interp(speed_ms, self.v[index - 1 : index + 1], self.t[index - 1 : index + 1]))
    def speed_at_time(self, time_s: float) -> float:
        """Find speed at time in s; return speed in m/s."""
        return np.interp(time_s, self.t, self.v)
    def distance_at_time(self, time_s: float) -> float:
        """Find distance at time in s; return distance in m."""
        return np.interp(time_s, self.t, self.x)

    def top_speed(self) -> float:
        """Find maximum recorded speed; return speed in m/s."""
        return float(np.max(self.v))

    def shift_points(self) -> np.ndarray:
        """Find gear shift points; return shift times in s."""
        changes = np.flatnonzero(np.diff(self.gear) != 0)
        return self.t[changes + 1]