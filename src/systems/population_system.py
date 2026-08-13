from systems.system import System


class PopulationSystem(System):
    def update(self, simulation):
        for civilization in simulation.civilizations:
            for colony in civilization.colonies:
                colony.population += 1