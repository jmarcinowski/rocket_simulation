"""Main driver file, runs sim"""
from object import Object
from rocket import Rocket
from force import Force
from globals import unit, Quantity, Q


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

        obj.apogee = max(obj.apogee, obj.y)
        obj.max_dy = max(obj.max_dy, obj.dy)


    def step(self, delta_t: float) -> float:
        """Runs one step of the simulation. Returns back the current time in sim"""
        for obj in self.objects:
            self.update_object(obj, delta_t)
        self.time += delta_t
        return self.time


    def apply_force(self, obj: Object, force:Force):
        """Sets the x and y acceleration of the obj provided the force. A = F / M."""
        force.x = force.x.to("newton")
        force.y = force.y.to("newton")
        obj.mass = obj.mass.to("kilogram")

        obj.ddx = (force.x / obj.mass).to("meter / second ** 2")
        obj.ddy = (force.y / obj.mass).to("meter / second ** 2")


    def apply_gimbal_force(self, rocket_obj: Rocket, amount_of_force:Quantity):
        """Rotates the rocket around CG from force applied at gimbal point"""
        tau = rocket_obj.radius_to_cg * amount_of_force

        rotational_acc = (tau / rocket_obj.moment_of_inertia)#.magnitude * unit.rad / unit.second ** 2
        rocket_obj.dd_theta = rotational_acc
        print(rotational_acc.to("rad/sec**2"))


rocket_obj = Rocket(
            # 27g = gimbal
            # 44.5g = https://estesrockets.com/products/d12-3-engines
            # 53g = other stuff exp. to add, just under legal limit iirc
            mass=    Q(27, "grams") \
                    +Q(44.5, "grams") \
                    +Q(53, "grams"),

            radius_to_cg = \
                    Q(50, "centimeter"),

            moment_of_inertia= 0.0144 * unit.kilogram * unit.meter**2,
            # moment_of_inertia= 0.0144 * unit.kilogram * unit.meter**2,
            # Engine: https://estesrockets.com/products/d12-3-engines
            thrust= Q(18, "newton"),

            burn_time= Q(2.09, "second"),

            theta=Q(0, "deg"),
        )


sim = Simulate([rocket_obj])
print(rocket_obj.mass.to("kilogram"))

gravity_force = Force().as_angle(
                            Q(180, "deg"),
                            Q(rocket_obj.mass.to("kilogram").magnitude * 9.81, "newton"))


def launch(rocket: Rocket):
    """Simulates a rocket launch. Provide with rocket object"""
    while True:
        t = sim.step(delta_t=Q(250, "millisecond"))
        if t < rocket.burn_time:
            thrust_force = Force().as_angle(rocket.theta, rocket.thrust)
            sim.apply_force(rocket, gravity_force + thrust_force)
        # elif t > rocket.burn_time and t < Q(19, "second"):
        #     sim.apply_force(rocket, gravity_force)
        else:
        #     rocket.theta = Q(315, "deg")
            sim.apply_force(rocket, gravity_force)
        # print("t:",t, "\tddy:",rocket.ddy, "\tdy:",rocket.dy, "\ty:",rocket.y)
        print(f"({rocket.x.magnitude}, {rocket.y.magnitude}),", end="")
        if rocket.y < 0 or t > Q(60, "second"):
            break


if False:
    sim = Simulate([rocket_obj])
    sim.apply_gimbal_force(rocket_obj, Q(0.41, "newton"))
    t = Q(0, "millisecond")
    while t < Q(3.5, "second"):

        if t < Q(1, "second"):
            sim.apply_gimbal_force(rocket_obj, Q(0.41, "newton"))
        elif t < Q(2,"second"):
            sim.apply_gimbal_force(rocket_obj, Q(0, "newton"))
        else:
            sim.apply_gimbal_force(rocket_obj, Q(-0.41, "newton"))
        
        
        print(f"{t}\tdd_theta: {rocket_obj.dd_theta}\t d_theta: {rocket_obj.d_theta}\t theta: {rocket_obj.theta}")
        t = sim.step(delta_t=Q(10, "millisecond"))

# launch(rocket_obj)
# print()
# print(rocket_obj.apogee.to("feet"))
# print(rocket_obj.apogee.to("miles"))
# print(rocket_obj.x.to("miles"))