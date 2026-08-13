from core.simulation import Simulation
import time
class Game:
    def __init__(self):
        self.simulation = Simulation()
        self.running = True


    """def run(self):
        while self.running:
            self.simulation.update()
            time.sleep(1)"""
            
    def run(self):
        for _ in range(3):
            self.simulation.update()
            time.sleep(1)
        