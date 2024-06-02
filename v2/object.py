"""Object class file"""
from dataclasses import dataclass
from globals import unit, Quantity, Q


@dataclass
class Object:
    """object that contains position/rotation/mass attributes"""
    x:Quantity = Q(0, "meter")
    y:Quantity = Q(0, "meter")
    dx:Quantity = Q(0, "meter / second")
    dy:Quantity = Q(0, "meter / second")
    ddx:Quantity = Q(0, "meter / second ** 2")
    ddy:Quantity = Q(0, "meter / second ** 2")

    theta:Quantity = Q(0, "deg")
    d_theta:Quantity = Q(0, "deg / second")
    dd_theta:Quantity = Q(0, "deg / second ** 2")

    mass:Quantity = 1 * unit.kilogram
    # https://www.omnicalculator.com/physics/mass-moment-of-inertia
    moment_of_inertia:Quantity = 0.0144 * unit.kilogram * unit.meter**2
    radius_to_gimbal:Quantity = 0.02 * unit.meter
    radius_to_cm:Quantity = 50 * unit.centimeter

    apogee = y
