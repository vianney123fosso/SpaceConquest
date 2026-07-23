class Colony:

    def __init__(self, name, planet):

        self.name = name
        self.planet = planet
        self.population = 100
        self.buildings = []

        self.resources = {
            "credits": 1000,
            "metal": 500,
            "tools": 100,
            "science": 0
        }


    def add_building(self, building):
        self.buildings.append(building)


    def __str__(self):

        output = (
            f"Colony: {self.name}\n"
            f"Population: {self.population}\n"
            f"Resources:\n"
        )

        for resource, value in self.resources.items():
            output += f"- {resource}: {value}\n"

        output += "Buildings:\n"

        for building in self.buildings:
            output += f"- {building}\n"

        return output