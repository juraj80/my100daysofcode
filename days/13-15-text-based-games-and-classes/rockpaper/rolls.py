class Roll:
    def __init__(self, name):
        self.name = name


class Scissors(Roll):
    def can_defeat(self, other_roll):
        if other_roll.name == 'Stone':
            return 'win'
        elif other_roll.name == self.name:
            return 'tie'
        else:
            return 'loose'


class Paper(Roll):
    def can_defeat(self, other_roll):
        if other_roll.name == 'Stone':
            return 'win'
        elif other_roll.name == self.name:
            return 'tie'
        else:
            return 'loose'


class Stone(Roll):
    def can_defeat(self, other_roll):
        if other_roll.name == 'Scissors':
            return 'win'
        elif other_roll.name == self.name:
            return 'tie'
        else:
            return 'loose'


class Player:
    def __init__(self, name, points):
        self.name = name
        self.points = points
