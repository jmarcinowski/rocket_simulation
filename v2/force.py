import math
from globals import unit, Quantity, Q


class Force:
    def __init__(self, x=Q(0, "newton"), y=Q(0, "newton")):
        self.x = x
        self.y = y
    def as_angle(self, angle:Quantity, mag:Quantity):
        self.x = math.sin(angle.to("rad")) * mag
        self.y = math.cos(angle.to("rad")) * mag

        return self
    
    def magnitude(self):
        return (self.x**2 + self.y**2)**0.5
    
    def __str__(self) -> str:
        return f"Force(x={self.x}, y={self.y})"
    
    def __add__(self, f2):
        return Force(self.x + f2.x, self.y + f2.y)


if __name__ == "__main__":
    g = Force().as_angle(Q(180, "deg"), Q(9.81, "newton"))
    a = Force(x=Q(3, "newton"), y=Q(4, "newton"))
    print(g + a)