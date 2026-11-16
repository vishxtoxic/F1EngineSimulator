"""Analysis declarations; internal units are SI: m, s, kg, N, W, and rad/s."""

import numpy as np

from .engine import Engine
from .environment import Environment
from .physics import air_relative_speed, drag_force, gradient_force, rolling_force
from .powertrain import select_gear, wheel_force
from .results import Result
from .simulate import derivative, simulate_run
from .vehicle import Vehicle


def equilibrium_top_speed(
    engine: Engine, vehicle: Vehicle, environment: Environment
) -> float:
    """Find equilibrium top speed for the model; return speed in m/s."""
    density = environment.pressure_pa / (287.058 * environment.temperature_k)

    def net_at(speed_ms: float) -> float:
        try:
            gear = select_gear(vehicle, engine, speed_ms)
            drive = wheel_force(engine, vehicle, speed_ms, gear)
        except ValueError:
            drive = 0.0
        losses = (
            drag_force(
                vehicle.cd_a_m2,
                air_relative_speed(speed_ms, environment.headwind_ms),
                density,
            )
            + rolling_force(vehicle.mass_kg, vehicle.rolling_coeff)
            + gradient_force(vehicle.mass_kg, environment.slope_rad)
        )
        return drive - losses

    low = 0.0
    high = 1.0
    while net_at(high) > 0 and high < 200.0:
        high *= 2
    if net_at(low) <= 0:
        return 0.0
    for _ in range(80):
        middle = (low + high) / 2
        if net_at(middle) > 0:
            low = middle
        else:
            high = middle
    return (low + high) / 2


def convergence_study(
    engine: Engine,
    vehicle: Vehicle,
    environment: Environment,
    time_steps_s: np.ndarray,
) -> np.ndarray:
    """Study time-step convergence in s; return convergence results."""
    steps = np.asarray(time_steps_s, dtype=float)
    if steps.ndim != 1 or np.any(steps <= 0):
        raise ValueError("time_steps_s must be a one-dimensional array of positive values")
    return np.array(
        [
            simulate_run(
                engine,
                vehicle,
                environment,
                derivative_fn=derivative,
                time_step_s=float(step),
            ).top_speed()
            for step in steps
        ]
    )


def energy_check(result: Result, vehicle: Vehicle) -> float:
    """Check result energy for a vehicle; return energy discrepancy in J."""
    initial_energy = 0.5 * vehicle.mass_kg * float(result.v[0]) ** 2
    final_energy = 0.5 * vehicle.mass_kg * float(result.v[-1]) ** 2
    return final_energy - initial_energy
