class human:
    def __init__(self):
        self.aggressivity = 10
        self.health = 100

    def injured(self, aggressivity):
        self.health = self.health - aggressivity
        self.aggressivity = self.aggressivity - 2

