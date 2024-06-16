"""Rocket class file"""
from dataclasses import dataclass
from globals import Quantity, Q, unit


@dataclass
class Rocket:
    """Rocket Object. Includes thrust, burn_time, and max_dy on top of the Object attributes"""
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
    radius_to_cg:Quantity = 50 * unit.centimeter

    apogee = y

    thrust:Quantity = 0
    burn_time:Quantity = 0
    max_dy:Quantity = Q(0, "meter / second")
    max_gimbal_angle:Quantity = Q(5, "degree")

    pid_gains5opt = {"P":-0.4330524, "D": -0.2854928}
    pid_gains10opt = {"P": -0.27639905, "D": -0.22370978} # 10 deg bank opt
    pid_gains45opt = {"P": -0.36878566, "D": -0.38102046} # 45 deg bank opt

