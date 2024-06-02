from globals import unit, Quantity, Q
from dataclasses import dataclass
from object import Object

@dataclass
class Rocket(Object):
    thrust:Quantity = 0
    burn_time:Quantity = 0
    max_dy:Quantity = Q(0, "meter / second")
    