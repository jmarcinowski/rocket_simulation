from object import Object
from simulate import Simulate
from vector import Vector
import json
import random

with open("rocket_config.json", "r", encoding="UTF-8") as f:
    rocket_config = json.load(f)

print(rocket_config)

rocket = Object()
sim = Simulate([rocket])
sim.apply_force_vector(rocket, Vector(10, 91))

while True:
    time = sim.step(delta_t=1/100)
    print(f"({rocket.x},{rocket.y}),",end="")

    if time > 1.6:
        sim.apply_force_vector(rocket, Vector(9.81, 270))

    if time > 5 or rocket.y < 0:
        break

print("Max alt: ", rocket.apogee)
