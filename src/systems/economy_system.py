from systems.system import System


class EconomySystem(System):

    def update(self, simulation):

        for civilization in simulation.civilizations:

            for colony in civilization.colonies:

                for building in colony.buildings:

                    building.produce(colony)