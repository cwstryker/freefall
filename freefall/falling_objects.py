"""
falling_objects.py

A collection of objects with defined mass and drag properties.
 
Developed by FIRST Robotics Competition Team 6343 - Steel Ridge Robotics

    Strong 
        Trustworthy
            Empowering
                Effective
                    Leadership

"""

from collections import namedtuple

FallingObject = namedtuple("FallingObject", ["mass", "drag"])


frc_power_cell = FallingObject(mass=0.15, drag=0.019)
