from celestial_object import CelestialObject
class Planet(CelestialObject):
    def __init__(self, image_path, mass, distance, orbit_speed, nucleo_status ):
        super().__init__(image_path=image_path,distance= distance, orbit_speed=orbit_speed, mass=mass)
        self.nucleo_status = nucleo_status
        
    def draw(self, screen):
        pass