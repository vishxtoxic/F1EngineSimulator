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
    rpm_points: np.ndarray | None = None
    torque_points_nm: np.ndarray | None = None

    def torque(self, rpm: float) -> float:
        """Return engine torque for rotational speed in rpm; return torque in N*m."""
        if rpm <= 0 or rpm < self.rpm_min or rpm > self.rpm_max:
            return 0.0
        if self.rpm_points is not None and self.torque_points_nm is not None:
            return float(np.interp(rpm, self.rpm_points, self.torque_points_nm))
        omega = rpm * 2 * np.pi / 60
        return self.power(rpm) / omega

    def power(self, rpm: float) -> float:
        """Return engine power for rotational speed in rpm; return power in W."""
        if rpm < self.rpm_min or rpm > self.rpm_max:
            return 0.0
        if self.rpm_points is not None and self.torque_points_nm is not None:
            return self.torque(rpm) * rpm * 2 * np.pi / 60
        if rpm <= self.rpm_peak_power:
            span = self.rpm_peak_power - self.rpm_min
            return self.peak_power_w * (rpm - self.rpm_min) / span
        span = self.rpm_max - self.rpm_peak_power
        return self.peak_power_w * (self.rpm_max - rpm) / span

    @classmethod
    def from_parametric(
        cls,
        peak_power_w: float,
        rpm_peak_power: float,
        rpm_max: float,
        rpm_min: float,
    ) -> "Engine":
        """Build an engine from power in W and speeds in rpm; return an Engine."""
        if peak_power_w <= 0:
            raise ValueError("peak_power_w must be positive")
        if not (0 < rpm_min < rpm_peak_power < rpm_max):
            raise ValueError("rpm values must satisfy 0 < min < peak < max")
        return cls(peak_power_w, rpm_peak_power, rpm_max, rpm_min)

    @classmethod
    def from_points(cls, rpm: np.ndarray, torque_nm: np.ndarray) -> "Engine":
        """Build an engine from rpm and torque points in N*m; return an Engine."""
        rpm = np.asarray(rpm, dtype=float)
        torque_nm = np.asarray(torque_nm, dtype=float)
        if rpm.ndim != 1 or torque_nm.ndim != 1 or rpm.size != torque_nm.size:
            raise ValueError("rpm and torque_nm must be one-dimensional arrays of equal length")
        if rpm.size < 2 or np.any(np.diff(rpm) <= 0) or np.any(torque_nm < 0):
            raise ValueError("rpm must be increasing and torque must be non-negative")
        power = torque_nm * rpm * 2 * np.pi / 60
        peak_index = int(np.argmax(power))
        return cls(
            float(power[peak_index]),
            float(rpm[peak_index]),
            float(rpm[-1]),
            float(rpm[0]),
            rpm,
            torque_nm,
        )
