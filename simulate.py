"""Simulation class file"""

from object import Object
from vector import Vector


class Simulate:
    """Simulation class"""
    def __init__(self, objects):
        self.objects = objects
        self.time = 0


    def update_object(self, obj: Object, delta_t: float) -> None:
        """Updates the position and rotation of a single Object"""
        obj.dx += obj.ddx * delta_t
        obj.dy += obj.ddy * delta_t

        obj.x += obj.dx * delta_t
        obj.y += obj.dy * delta_t

        obj.d_theta += obj.dd_theta * delta_t
        obj.theta += obj.d_theta * delta_t

        obj.apogee = max(obj.apogee, obj.y)


    def step(self, delta_t: float) -> float:
        """Runs one step of the simulation. Returns back the current time in sim"""
        for obj in self.objects:
            self.update_object(obj, delta_t)
        self.time += delta_t
        return self.time


    def apply_force_vector(self, obj: Object, vector: Vector) -> None:
        """Apply force vector"""
        # f = ma
        # a = f / m
        (f_x, f_y) = vector.components()
        obj.ddx = f_x / obj.mass
        obj.ddy = f_y / obj.mass


def test_gravity():
    """Test physics: NOT including torque"""
    # Object falls for 10 seconds
    obj = Object(ddy=-9.81)
    sim = Simulate([obj])
    while sim.step(delta_t=1/10000) < 10:
        pass
    # check if ended up in correct spot
    assert round(obj.y, 1) == -490.5
    assert obj.x == 0
    # check final velocity
    assert round(obj.dy, 1) == -98.1
    assert obj.dx == 0
