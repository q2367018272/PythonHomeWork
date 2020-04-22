class dog:
    def __init__(self):
        self.aggressivity=15
        self.health=80
    def injured(self,aggressivity):
        self.health=self.health-aggressivity
        self.aggressivity=self.aggressivity-3

