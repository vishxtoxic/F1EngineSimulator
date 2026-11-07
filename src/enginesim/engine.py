"""Engine declarations; internal units are SI: m, s, kg, N, W, and rad/s."""

from dataclasses import dataclass

import numpy as np


@dataclass
class Engine:
    """Describe an engine using a parametric power curve."""

    peak_power_w: float
    rpm_peak_power: float
    rpm_max: float
    rpm_min: float

    def torque(self, rpm: float) -> float:
        """Return engine torque for rotational speed in rpm; return torque in N*m."""
        raise NotImplementedError("TODO")

    def power(self, rpm: float) -> float:
        """Return engine power for rotational speed in rpm; return power in W."""
        raise NotImplementedError("TODO")

    @classmethod
    def from_parametric(
        cls,
        peak_power_w: float,
        rpm_peak_power: float,
        rpm_max: float,
        rpm_min: float,
    ) -> "Engine":
        """Build an engine from power in W and speeds in rpm; return an Engine."""
        raise NotImplementedError("TODO")

    @classmethod
    def from_points(cls, rpm: np.ndarray, torque_nm: np.ndarray) -> "Engine":
        """Build an engine from rpm and torque points in N*m; return an Engine."""
        raise NotImplementedError("TODO")
