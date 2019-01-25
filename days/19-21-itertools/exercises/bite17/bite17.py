'''
Write a function called friends_teams that takes a list of friends, a team_size (type int, default=2) and order_does_matter (type bool, default False).

Return all possible teams. Hint: if order matters (order_does_matter=True), the number of teams would be greater.
'''

from itertools import combinations, permutations


def friends_teams(friends, team_size=2, order_does_matter=False):
    if order_does_matter:
        func = permutations
    else:
        func = combinations
    return list(func(friends, team_size))

