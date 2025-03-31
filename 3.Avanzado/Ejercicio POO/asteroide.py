from celestial_object import CelestialObject
class Asteroide(CelestialObject):
    def __init__(self, images, distance, orbit_speed, mass):
        super().__init__(images=images,distance=distace,orbit_speed=orbit_speed, mass=mass)
    
    def __init__(self, images,distance,orbit_speed, mass):
        self.images = images
        self.distance = distance
        self.orbit_speed = orbit_speed
        self.mass = mass
    