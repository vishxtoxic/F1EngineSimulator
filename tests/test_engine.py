import math

import numpy as np
import pytest


def test_power_equals_torque_times_omega() -> None:
    from enginesim.engine import Engine

    engine = Engine.from_parametric(100_000, 8_000, 12_000, 1_000)
    rpm = 8_000
    assert math.isclose(engine.power(rpm), engine.torque(rpm) * rpm * 2 * math.pi / 60)


def test_peak_at_set_rpm() -> None:
    from enginesim.engine import Engine

    engine = Engine.from_parametric(100_000, 8_000, 12_000, 1_000)
    assert engine.power(8_000) == 100_000


def test_zero_above_limiter() -> None:
    from enginesim.engine import Engine

    engine = Engine.from_parametric(100_000, 8_000, 12_000, 1_000)
    assert engine.power(12_001) == 0
    assert engine.torque(12_001) == 0


def test_bad_inputs_raise() -> None:
    from enginesim.engine import Engine

    with pytest.raises(ValueError):
        Engine.from_parametric(0, 8_000, 12_000, 1_000)
    with pytest.raises(ValueError):
        Engine.from_points(np.array([2_000, 1_000]), np.array([100, 100]))
