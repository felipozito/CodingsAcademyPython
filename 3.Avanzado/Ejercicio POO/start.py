from celestial_object import CelestialObject
class Start(CelestialObject):
    def __init__(self, images, nucleo_status, orbit_speed, mass):
        super().__init__(images=images, mass=mass)