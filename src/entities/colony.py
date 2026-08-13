class Colony:

    def __init__(self, name):

        self.name = name
        self.population = 100
        self.resources = {
            "money": 1000,
            "metal": 500,
            "energy": 100
        }

        self.buildings = []
        self.technologies = []
        
    def __str__(self):
        return f"name: {self.name}, population:{self.population}, resources: {self.resources}"
    