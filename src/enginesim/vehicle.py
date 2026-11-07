"""Vehicle declarations; internal units are SI: m, s, kg, N, W, and rad/s."""

from dataclasses import dataclass

import numpy as np


@dataclass
class Vehicle:
    """Describe vehicle parameters using SI units."""

    mass_kg: float
    cd_a_m2: float
    rolling_coeff: float
    wheel_radius_m: float
    overall_ratios: np.ndarray
    driveline_efficiency: float
    friction_coeff: float
    driven_weight_fraction: float
    launch_rpm: float
