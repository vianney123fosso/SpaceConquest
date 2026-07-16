import time
from core.clock import Clock
from world.universe import Universe
from world.solar_system import SolarSystem
from world.star import Star
from world.planet import Planet
from entities.colony import Colony
from entities.civilization import Civilization

class Simulation:
    def __init__(self):
        self.clock = Clock()
        self.universe = Universe()
        self.initialize_universe()
        """self.systems = [
            EconomySystem(),
            ResearchSystem(),
            PopulationSystem(),
            PhysicsSystem()
        ]"""
        
     
    
    def initialize_universe(self):
        print("INITIALISATION DE L'UNIVERS")
        
        sun = Star("Sun",mass=1.989e30,temperature=5778)
        
        solar_system = SolarSystem("Sol",sun)
        
        earth = Planet("Earth",mass=5.972e24,radius=6371)
        
        humanity = Civilization("Humanity")
        earth_colony = Colony("Earth Colony",earth)
        humanity.add_colony(earth_colony)

        self.civilizations = [humanity]
        """human_colony = Colony("Earth Colony")
        earth.add_colony(human_colony)"""
        
        mars = Planet("Mars",mass=6.39e23,radius=3389)
        
        solar_system.add_planet(earth)
        solar_system.add_planet(mars)
        self.universe.add_solar_system(solar_system)

    def update(self):
        self.clock.advance(1)
        self.universe.display()
        print("Simulation time :", self.clock.time)
        """for system in self.systems:
            system.update(self.universe)"""
        
        print("Civilizations:")

        for civilization in self.civilizations:
            print(civilization)
            
    



    