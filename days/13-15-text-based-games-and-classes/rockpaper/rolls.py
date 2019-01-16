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

#
# class Scissors(Roll):
#     def can_defeat(self, other_roll):
#         if other_roll.name == 'Rock':
#             return 'win'
#         elif other_roll.name == self.name:
#             return 'draw'
#         else:
#             return 'loose'
#
#
# class Paper(Roll):
#     def can_defeat(self, other_roll):
#         if other_roll.name == 'Rock':
#             return 'win'
#         elif other_roll.name == self.name:
#             return 'draw'
#         else:
#             return 'loose'
#
#
# class Rock(Roll):
#     def can_defeat(self, other_roll):
#         if other_roll.name == 'Scissors':
#             return 'win'
#         elif other_roll.name == self.name:
#             return 'draw'
#         else:
#             return 'loose'


class Player:
    def __init__(self, name, points):
        self.name = name
        self.points = points
