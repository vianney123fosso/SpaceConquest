class Universe:
    
    def __init__(self):
        self.solar_systems = []
        
    def add_solar_system(self, solar_system):
        self.solar_systems.append(solar_system)
        
    def display(self):

        for system in self.solar_systems:
            print("System:", system.name)
            print("Star:", system.star.name)
            print("Planets:")
            for planet in system.planets:
                print(planet)

      
            

        
    
       
   
        
        
