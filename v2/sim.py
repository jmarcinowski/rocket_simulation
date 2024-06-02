import random
from object import Object
from rocket import Rocket
from force import Force
from globals import unit, Quantity, Q
import math



class Simulate:
    """Simulation class"""
    def __init__(self, objects):
        self.objects = objects
        self.time = 0


    def update_object(self, obj: Rocket, delta_t: Quantity) -> None:
        """Updates the position and rotation of a single Object"""
        delta_t = delta_t.to("second")

        obj.dx += (obj.ddx * delta_t).to("meters / second")
        obj.dy += (obj.ddy * delta_t).to("meters / second")

        obj.x += (obj.dx * delta_t).to("meters")
        obj.y += (obj.dy * delta_t).to("meters")

        obj.d_theta += obj.dd_theta * delta_t
        obj.theta += obj.d_theta * delta_t

        # obj.theta = obj.theta % 360

        obj.apogee = max(obj.apogee, obj.y)
        obj.max_dy = max(obj.max_dy, obj.dy)


    def step(self, delta_t: float) -> float:
        """Runs one step of the simulation. Returns back the current time in sim"""
        for obj in self.objects:
            self.update_object(obj, delta_t)
        self.time += delta_t
        return self.time
    

    def apply_force(self, obj: Object, force:Force):
        force.x = force.x.to("newton")
        force.y = force.y.to("newton")
        obj.mass = obj.mass.to("kilogram")

        obj.ddx = (force.x / obj.mass).to("meter / second ** 2")
        obj.ddy = (force.y / obj.mass).to("meter / second ** 2")

    # def apply_tangential_force(self)


rocket = Rocket(
            # 27g = gimbal
            # 44.5g = https://estesrockets.com/products/d12-3-engines
            # 76g = other stuff exp. to add, just under legal limit iirc
            mass=    Q(27, "grams") \
                    +Q(44.5, "grams") \
                    +Q(53, "grams"),

            radius_to_cm = \
                    Q(50, "centimeter"),
            
            moment_of_inertia= \
                    0.0144 * unit.kilogram * unit.meter**2,
            # Engine: https://estesrockets.com/products/d12-3-engines
            thrust= Q(12, "newton"),
            
            burn_time= \
                    Q(1.6, "second"),
        )


sim = Simulate([rocket])
print(rocket.mass.to("kilogram"))

gravity_force = Force().as_angle(
                                    Q(180, "deg"),
                                    Q(rocket.mass.to("kilogram").magnitude * 9.81, "newton"))


def launch(rocket: Rocket):
    while True:
        t = sim.step(delta_t=Q(10, "millisecond"))
        if t < rocket.burn_time:
            thrust_force = Force().as_angle(rocket.theta, rocket.thrust)
            sim.apply_force(rocket, gravity_force + thrust_force)
        else:
            sim.apply_force(rocket, gravity_force)
        print("t:",t, "\tddy:",rocket.ddy, "\tdy:",rocket.dy, "\ty:",rocket.y)
        if rocket.y < 0:
            break
