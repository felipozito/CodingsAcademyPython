import pygame
from celestial_object import CelestialObject
class Star(CelestialObject):
    def __init__(self, image_path, mass, nucleo_status,):
        super().__init__(image_path=image_path, mass=mass,)
        self.nucleo_status=nucleo_status
        
    def draw(self, screen):
        pass