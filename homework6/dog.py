class dog:
    def __init__(self):
        self.aggressivity=15
        self.health=80
    def injured(self,aggressivity):
        self.health=self.health-aggressivity
        if not (aggressivity==0):
            self.aggressivity=self.aggressivity-3
        if(self.aggressivity<0):
            self.aggressivity=0

