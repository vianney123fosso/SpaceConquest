class SolarSystem:

    def __init__(self, name, star):
        self.name = name
        self.star = star
        self.planets = []


    def add_planet(self, planet):
        self.planets.append(planet)