# F1 Engine Simulator

A small longitudinal vehicle-performance simulator using SI units internally.

## Install

```text
python -m pip install -e ".[dev]"
```

## Quick example

```python
import numpy as np

from enginesim import Engine, Environment, Vehicle
from enginesim.simulate import derivative, simulate_run

engine = Engine.from_parametric(750_000, 10_500, 13_000, 1_000)
vehicle = Vehicle(
    mass_kg=800,
    cd_a_m2=1.5,
    rolling_coeff=0.015,
    wheel_radius_m=0.33,
    overall_ratios=np.array([3.2, 2.4, 1.8, 1.4, 1.1, 0.9]),
    driveline_efficiency=0.95,
    friction_coeff=1.5,
    driven_weight_fraction=0.5,
    launch_rpm=4_000,
)
environment = Environment(temperature_k=288.15, pressure_pa=101_325, headwind_ms=0, slope_rad=0)
result = simulate_run(engine, vehicle, environment, derivative)
print(result.time_to_speed(100 / 3.6))
print(result.top_speed())
```

## Model

The model includes engine power, gearing, traction, aerodynamic drag, rolling resistance,
road gradient, and fixed-step RK4 integration. Times are seconds, distances metres,
speeds metres per second, engine speeds rpm, and forces Newtons.

## Tests

```text
python -m pytest
```
