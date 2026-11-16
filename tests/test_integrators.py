import math

import numpy as np


def _decay(_t: float, state: np.ndarray) -> np.ndarray:
    del _t
    return -state


def test_euler_matches_exponential_decay() -> None:
    from enginesim.integrators import euler_step

    result = euler_step(np.array([1.0]), _decay, 0, 0.1)
    assert np.allclose(result, [0.9])


def test_rk4_matches_exponential_decay() -> None:
    from enginesim.integrators import rk4_step

    result = rk4_step(np.array([1.0]), _decay, 0, 0.1)
    assert np.allclose(result, [math.e ** -0.1], rtol=1e-4)
