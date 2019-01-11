games_won = dict(sara=0, bob=1, tim=5, julian=3, jim=1)


def print_game_stats(games_won=games_won):
    """Loop through games_won's dict k, v pairs (items) and
       print how many games each person has won, pluralize
       'game' based on number"""
    for name, score in games_won.items():
        if score ==1:
            print(f'{name} has won {score} game')
        else:
            print(f'{name} has won {score} games')

if __name__ == '__main__':
    print_game_stats()