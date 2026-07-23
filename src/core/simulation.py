import time
from core.clock import Clock
from world.universe import Universe
from world.solar_system import SolarSystem
from world.star import Star
from world.planet import Planet
from entities.colony import Colony
from entities.civilization import Civilization
from systems.population_system import PopulationSystem
from entities.building import Mine, Factory, Laboratory
from systems.economy_system import EconomySystem

class Simulation:
    def __init__(self):
        self.clock = Clock()
        self.universe = Universe()
        self.civilizations=[]
        self.systems = [
            PopulationSystem(),
            EconomySystem()
        ]
        self.initialize_universe()
        
     
    
    def initialize_universe(self):
        print("INITIALISATION DE L'UNIVERS")
        humanity = Civilization("Humanity")
        self.civilizations = [humanity]
        
        
        #humanity.add_colony(earth_colony)
    
        #------------------------------- INITIALIZING EARTH----------------------------
        
        earth = Planet(name="Earth",mass=5.972e24,radius=6371,gravity=9.81,atmosphere="Nitrogen/Oxygen",habitability=1.0,orbital_radius=149.6e9,resources={"metal": 70,"energy": 100,"science": 80})
        earth_colony = Colony("Earth Colony",earth)
        humanity.add_colony(earth_colony)
        earth_colony.add_building(Mine())
        earth_colony.add_building(Mine())
        earth_colony.add_building(Factory())
        earth_colony.add_building(Laboratory())
        #-------------------------------------------------------------------------------
        
        #-----------------------------INITIALIZING MARCH---------------------------------
        mars = Planet(name="Mars",mass=6.39e23,radius=3389,gravity=3.71,atmosphere="CO2",habitability=0.3,orbital_radius=227.9e9,resources={"metal": 80,"energy": 40,"science": 60})
        #---------------------------------------------------------------------------------
        
        #-----------------------------INITIALIZING SOLAR SYSTEM-------------------------
        sun = Star("Sun",mass=1.989e30,temperature=5778)
        
        solar_system = SolarSystem("Sol",sun)
        solar_system.add_planet(earth)
        solar_system.add_planet(mars)
        self.universe.add_solar_system(solar_system)
        #-------------------------------------------------------------------------------
        
       

        
        
        
        
    def update(self):

        self.clock.advance(1)
        for system in self.systems:
            system.update(self)
        print(f"Time : {self.clock.time}")
        for civilization in self.civilizations:
            print(civilization)

            
    



    