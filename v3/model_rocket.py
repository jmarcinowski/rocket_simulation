from globals import Q, unit
from rocket import Rocket

model_rocket = Rocket(
            # 27g = gimbal
            # 44.5g = https://estesrockets.com/products/d12-3-engines
            # 53g = other stuff exp. to add, just under legal limit iirc
            mass=    Q(27, "grams") \
                    +Q(44.5, "grams") \
                    +Q(53, "grams"),

            radius_to_cg = \
                    Q(50, "centimeter"),

            moment_of_inertia= 1 * unit.kilogram * unit.meter**2,
            # moment_of_inertia= 0.0144 * unit.kilogram * unit.meter**2,
            # Engine: https://estesrockets.com/products/d12-3-engines
            thrust= Q(12, "newton"),

            burn_time= Q(1.6, "second"),

            theta=Q(3, "deg"),
            max_gimbal_angle=Q(5, "degree")
        )