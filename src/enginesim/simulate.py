"""Simulation declarations; internal units are SI: m, s, kg, N, W, and rad/s."""

from collections.abc import Callable

import numpy as np

from .engine import Engine
from .environment import Environment
from .environment import air_density
from .integrators import rk4_step
from .physics import (
    air_relative_speed,
    drag_force,
    gradient_force,
    max_traction_force,
    net_force,
    rolling_force,
)
from .powertrain import engine_rpm, select_gear, wheel_force
from .results import Result
from .vehicle import Vehicle


def evaluate_forces(
    state: np.ndarray, engine: Engine, vehicle: Vehicle, environment: Environment
) -> np.ndarray:
    """Evaluate forces for a state containing SI quantities; return force values in N."""
    speed_ms = max(float(state[0]), 0.0)
    gear = select_gear(vehicle, engine, speed_ms)
    drive = min(
        wheel_force(engine, vehicle, speed_ms, gear),
        max_traction_force(
            vehicle.mass_kg,
            vehicle.friction_coeff,
            vehicle.driven_weight_fraction,
        ),
    )
    density = air_density(environment.temperature_k, environment.pressure_pa)
    drag = drag_force(
        vehicle.cd_a_m2,
        air_relative_speed(speed_ms, environment.headwind_ms),
        density,
    )
    rolling = rolling_force(vehicle.mass_kg, vehicle.rolling_coeff)
    gradient = gradient_force(vehicle.mass_kg, environment.slope_rad)
    return np.array([net_force(drive, drag, rolling, gradient), drive, drag, rolling, gradient])


def derivative(
    _t: float,
    state: np.ndarray,
    engine: Engine,
    vehicle: Vehicle,
    environment: Environment,
) -> np.ndarray:
    """Evaluate the state derivative at time t in s; return SI state rates."""
    del _t
    forces = evaluate_forces(state, engine, vehicle, environment)
    acceleration = forces[0] / vehicle.mass_kg
    if state[0] <= 0 and acceleration < 0:
        acceleration = 0.0
    return np.array([acceleration, max(float(state[0]), 0.0)])


def stop_at_time(t: float, _state: np.ndarray, limit_s: float) -> bool:
    """Check time t in s against a time limit in s; return whether to stop."""
    del _state
    return t >= limit_s


def stop_at_speed(_t: float, state: np.ndarray, limit_ms: float) -> bool:
    """Check state speed in m/s against a limit in m/s; return whether to stop."""
    del _t
    return state[0] >= limit_ms


def stop_at_distance(_t: float, state: np.ndarray, limit_m: float) -> bool:
    """Check state distance in m against a limit in m; return whether to stop."""
    del _t
    return state[1] >= limit_m


def simulate_run(
    engine: Engine,
    vehicle: Vehicle,
    environment: Environment,
    derivative_fn: Callable[
        [float, np.ndarray, Engine, Vehicle, Environment], np.ndarray
    ],
    time_step_s: float = 0.01,
    duration_s: float = 30.0,
) -> Result:
    """Run a simulation from the supplied model objects; return a Result."""
    if time_step_s <= 0 or duration_s <= 0:
        raise ValueError("time_step_s and duration_s must be positive")
    times = [0.0]
    states = [np.array([0.0, 0.0])]
    steps = int(np.ceil(duration_s / time_step_s))
    for steps in range(steps):
        t = times[-1]
        dt = min(time_step_s, duration_s - t)
        if dt <= 0:
            break
        def bound_derivative(current_t: float, current_state: np.ndarray) -> np.ndarray:
            return derivative_fn(
                current_t, current_state, engine, vehicle, environment
            )

        state = rk4_step(
            states[-1],
            bound_derivative,
            t,
            dt,
        )
        state[0] = max(state[0], 0.0)
        state[1] = max(state[1], states[-1][1])
        states.append(state)
        times.append(t + dt)
    state_array = np.asarray(states)
    speeds = state_array[:, 0]
    gears = np.array([select_gear(vehicle, engine, speed) for speed in speeds], dtype=int)
    rpms = np.array(
        [
            engine_rpm(
                float(speed),
                vehicle.wheel_radius_m,
                float(vehicle.overall_ratios[int(gear)]),
            )
            for speed, gear in zip(speeds, gears)
        ]
    )
    return Result(np.asarray(times), speeds, state_array[:, 1], gears, rpms)
