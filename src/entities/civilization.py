from systems.population_system import PopulationSystem

class Civilization:

    def __init__(self, name):

        self.name = name
        self.colonies = []
        self.systems = [PopulationSystem()]


    def add_colony(self, colony):
        self.colonies.append(colony)


    def __str__(self):
        output = f"Civilization: {self.name}\n"
        output += "Colonies:\n"
        for colony in self.colonies:
            output += (f"- {colony.name} "
            f"(Population : {colony.population})\n"
            )

        return output