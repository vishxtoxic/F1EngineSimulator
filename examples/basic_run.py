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
environment = Environment(288.15, 101_325, 0, 0)
result = simulate_run(engine, vehicle, environment, derivative)

print(f"0-100 km/h: {result.time_to_speed(100 / 3.6):.2f} s")
print(f"Top speed: {result.top_speed() * 3.6:.1f} km/h")
