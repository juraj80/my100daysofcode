class Roll:
    def __init__(self, name):
        self.name = name

    def can_defeat(self, other_roll):
        wins = {
            'Rock':'Scissors',
            'Scissors': 'Paper',
            'Paper': 'Rock',
        }
        if wins[self.name] == other_roll.name:
            return True
        else:
            return False


class Player:
    def __init__(self, name, points):
        self.name = name
        self.points = points
