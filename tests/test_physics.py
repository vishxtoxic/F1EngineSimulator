import math


def test_drag_scales_with_speed_squared() -> None:
    from enginesim.physics import drag_force

    assert math.isclose(drag_force(1, 20, 1), 4 * drag_force(1, 10, 1))


def test_zero_speed_zero_drag() -> None:
    from enginesim.physics import drag_force

    assert drag_force(1, 0, 1) == 0


def test_rolling_force_value() -> None:
    from enginesim.physics import rolling_force

    assert math.isclose(rolling_force(1000, 0.01), 98.1)


def test_traction_limit_value() -> None:
    from enginesim.physics import max_traction_force

    assert math.isclose(max_traction_force(1000, 1, 0.5), 4905)
