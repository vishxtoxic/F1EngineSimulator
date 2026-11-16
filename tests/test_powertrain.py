import numpy as np


def test_rpm_per_gear_hand_values() -> None:
    from enginesim.powertrain import engine_rpm

    assert np.isclose(engine_rpm(10, 0.5, 2), 381.97, atol=0.01)


def test_select_gear_best_force() -> None:
    from enginesim.engine import Engine
    from enginesim.powertrain import select_gear
    from enginesim.vehicle import Vehicle

    engine = Engine.from_parametric(100_000, 8_000, 12_000, 1_000)
    vehicle = Vehicle(800, 1, 0.01, 0.3, np.array([3.0, 2.0]), 0.9, 1, 0.5, 4_000)
    assert select_gear(vehicle, engine, 5) == 0


def test_no_gear_above_limiter() -> None:
    from enginesim.engine import Engine
    from enginesim.powertrain import gear_options
    from enginesim.vehicle import Vehicle

    engine = Engine.from_parametric(100_000, 8_000, 12_000, 1_000)
    vehicle = Vehicle(800, 1, 0.01, 0.3, np.array([4.0, 2.0]), 0.9, 1, 0.5, 4_000)
    assert np.array_equal(gear_options(vehicle, 100, engine), np.array([1]))
