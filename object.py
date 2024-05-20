"""Object class file"""
from dataclasses import dataclass


@dataclass
class Object:
    """object that contains position/rotation/mass attributes"""
    x:float = 0
    y:float = 0
    dx:float = 0
    dy:float = 0
    ddx:float = 0
    ddy:float = 0

    theta:float = 0
    d_theta:float = 0
    dd_theta:float = 0

    mass:float = 1

    apogee = y
