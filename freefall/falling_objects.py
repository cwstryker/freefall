from collections import namedtuple

FallingObject = namedtuple("FallingObject", ["mass", "drag"])


frc_power_cell = FallingObject(mass=0.15, drag=0.019)
