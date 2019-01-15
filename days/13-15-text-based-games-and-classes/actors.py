class Creature:
    def __init__(self,name,level):
        self.name = name
        self.level = level

    def defensive_roll(self):
        return random.randint(0,12)*self.level

