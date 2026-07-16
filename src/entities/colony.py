class Colony:

    def __init__(self, name, planet):

        self.name = name
        self.planet = planet

        self.population = 100

        self.resources = {
            "money": 1000,
            "metal": 500,
            "energy": 100
        }

        self.buildings = []

        self.technologies = []


    def __str__(self):

        return (
            f"Colony: {self.name}\n"
            f"Location: {self.planet.name}\n"
            f"Population: {self.population}"
        )