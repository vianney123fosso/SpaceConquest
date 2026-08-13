class Planet:

    def __init__(self, name, mass, radius):
        self.name = name
        self.mass = mass
        self.radius = radius

        self.colonies = []
        
    def add_colony(self, colony):
        self.colonies.append(colony)
        
    def __str__(self):
        output=f" Name:{self.name}\n Mass:{self.mass}\n Radius: {self.radius}\n This planet holds:"
        for colony in self.colonies:
            output+=f"{colony}\n"
        return output
        
        