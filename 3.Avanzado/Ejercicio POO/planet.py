import pygame
from .celestial_object import CelestialObject


class Planet(CelestialObject):
    def __init__(self,images,distance,orbit_speed, mass, nucleo_status):
        super().__init__(images=images,distance=distace,orbit_speed=orbit_speed, mass=mass)
        self.nucleo_status = nucleo_status
        
        
