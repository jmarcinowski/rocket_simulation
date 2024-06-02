"""Contains Force class"""
import math
from globals import Quantity, Q


class Force:
    """
    Force class, keeps track of Force.x, Force,y.
    Allows you to create a Force object with Force().as_angle(Quantity, Quantity).
    Allows you to get the magnitude of the vector with Force.magnitude
    """


    def __init__(self, x=Q(0, "newton"), y=Q(0, "newton")):
        self.x = x
        self.y = y


    def as_angle(self, angle:Quantity, mag:Quantity):
        """
        **Requires Quantity objects!
        angle - Quantity(amount, "unit")
        mag - Quantity(amount, "unit")
        Returns - Force object
        """
        self.x = math.sin(angle.to("rad")) * mag
        self.y = math.cos(angle.to("rad")) * mag

        return self


    def magnitude(self):
        """Returns - magnitude of the vector as a float."""
        return (self.x**2 + self.y**2)**0.5


    def __str__(self) -> str:
        return f"Force(x={self.x}, y={self.y})"


    def __add__(self, f2):
        return Force(self.x + f2.x, self.y + f2.y)
