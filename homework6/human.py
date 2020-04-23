class human:
    def __init__(self):
        self.aggressivity = 10
        self.health = 100

    def injured(self, aggressivity):
        self.health = self.health - aggressivity
        if not (aggressivity==0):
            self.aggressivity = self.aggressivity - 2
        if (self.aggressivity < 0):
            self.aggressivity = 0

