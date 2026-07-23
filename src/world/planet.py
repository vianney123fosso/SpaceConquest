class Planet:

    def __init__(
        self,
        name,
        mass,
        radius,
        gravity,
        atmosphere,
        habitability,
        orbital_radius,
        resources
    ):

        self.name = name

        # Caractéristiques physiques
        self.mass = mass          # kg
        self.radius = radius      # km
        self.gravity = gravity    # m/s²

        # Conditions de vie
        self.atmosphere = atmosphere
        self.habitability = habitability

        # Position dans le système
        self.orbital_radius = orbital_radius  # mètres

        # Ressources naturelles
        self.resources = resources


    def __str__(self):

        return (
            f"Planet: {self.name}\n"
            f"Mass: {self.mass} kg\n"
            f"Radius: {self.radius} km\n"
            f"Gravity: {self.gravity} m/s²\n"
            f"Atmosphere: {self.atmosphere}\n"
            f"Habitability: {self.habitability}\n"
            f"Orbital radius: {self.orbital_radius} m\n"
            f"Resources: {self.resources}\n"
        )