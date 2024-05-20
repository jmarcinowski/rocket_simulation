"""Vector class file"""


import math

class Vector:
    """Vector class"""
    def __init__(self, mag, angle_deg):
        self.mag = mag
        self.angle_deg = angle_deg % 360
        self.angle_rad = math.radians(angle_deg)


    def components(self, ndigits=3):
        """0 degrees -> on the x-axis"""

        x = math.cos(self.angle_rad) * self.mag
        y = math.sin(self.angle_rad) * self.mag

        x = round(x, ndigits)
        y = round(y, ndigits)

        return (x, y)


def test_vectors():
    """Test the vector components method"""

    assert Vector(10, 0).components() == (10, 0)
    assert Vector(10, 90).components() == (0,10)
    assert Vector(10, 180).components() == (-10, 0)
    assert Vector(10, 270).components() == (0, -10)

    assert Vector(10, 360).components() == (10, 0)
    assert Vector(10, -180).components() == (-10, 0)

    assert Vector(10, 360 * 18).components() == (10, 0)

    assert Vector(0,0).components() == (0,0)

    assert Vector(-10, 0).components() == (-10, 0)
