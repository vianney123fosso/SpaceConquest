class Planet:

    def __init__(self, name, mass, radius):

        self.name = name
        self.mass = mass
        self.radius = radius


    def __str__(self):

        return (
            f"Planet: {self.name}\n"
            f"Mass: {self.mass}\n"
            f"Radius: {self.radius} km"
        )
        