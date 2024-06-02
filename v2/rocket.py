"""Rocket class file"""
from dataclasses import dataclass
from globals import Quantity, Q
from object import Object


@dataclass
class Rocket(Object):
    """Rocket Object. Includes thrust, burn_time, and max_dy on top of the Object attributes"""
    thrust:Quantity = 0
    burn_time:Quantity = 0
    max_dy:Quantity = Q(0, "meter / second")
