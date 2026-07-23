class Building:

    def __init__(self, name):
        self.name = name

    def produce(self, colony):
        pass

    def __str__(self):
        return self.name


class Mine(Building):

    def __init__(self):
        super().__init__("Mine")

    def produce(self, colony):
        colony.resources["metal"] += 20


class Factory(Building):

    def __init__(self):
        super().__init__("Factory")

    def produce(self, colony):
        colony.resources["tools"] += 10


class Laboratory(Building):

    def __init__(self):
        super().__init__("Laboratory")

    def produce(self, colony):
        colony.resources["science"] += 5