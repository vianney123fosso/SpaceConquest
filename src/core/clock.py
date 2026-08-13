class Clock:
    def __init__(self):
        self.time = 0.0
        self.time_scale = 1.0

    def advance(self, dt: float):
        self.time += dt * self.time_scale