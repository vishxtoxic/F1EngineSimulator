import math


def test_rpm_to_rad_s() -> None:
    from enginesim.units import rpm_to_rad_s

    assert math.isclose(rpm_to_rad_s(60), 2 * math.pi)


def test_rad_s_to_rpm() -> None:
    from enginesim.units import rad_s_to_rpm

    assert math.isclose(rad_s_to_rpm(2 * math.pi), 60)


def test_kmh_to_ms() -> None:
    from enginesim.units import kmh_to_ms

    assert kmh_to_ms(36) == 10


def test_ms_to_kmh() -> None:
    from enginesim.units import ms_to_kmh

    assert ms_to_kmh(10) == 36
