from rolls import Scissors, Paper, Stone, Player
import random

def main():
    print_header()
    rolls = build_the_three_rolls()

    name = get_players_name()

    player1 = Player(name,0)
    player2 = Player("computer",0)

    game_loop(player1,player2,rolls)



def print_header():
    print('-------------------------------')
    print('    Rock, Paper, Scissors')
    print('-------------------------------')


def get_players_name():
    name = input('Type your name here, please: ')
    return name

def build_the_three_rolls():
    r1 = Scissors('Scissors')
    r2 = Paper('Paper')
    r3 = Stone('Stone')
    return [r1,r2,r3]

def game_loop(p1,p2,rolls):
    count = 0
    print(f"OK, let's play a game {p1.name}!!! ")
    print()

    while count < 3:
        p2_roll = random.choice(rolls)

        p1_roll = input("Choose [s]tone, [p]aper, or s[c]issors: ").lower()
        if p1_roll == 's':
            p1_roll = rolls[2]
        elif p1_roll == 'p':
            p1_roll = rolls[1]
        elif p1_roll == 'c':
            p1_roll = rolls[0]
        else:
            print('Wrong input !!!')
            break
        print()
        # display throws
        print(f'{p1.name} throws {p1_roll.name}')
        print(f'Computer throws {p2_roll.name}')
        print()
        outcome = p1_roll.can_defeat(p2_roll)
        # display winner for this round

        if outcome == 'win':
            p1.points+=1
            print(f'{p1.name} wins round {count+1} and have {p1.points} points')
        elif outcome == 'loose':
            p2.points+=1
            winner = 'Computer'
            print(f'Computer wins round {count+1} and have {p2.points} points')
        else:
            print('Tie')
            count-=1

        count += 1
        print()

    # display winner for this round
    if p1.points > p2.points:
        print(f'{p1.name} won the whole game with {p1.points} points!!!')
    else:
        print(f'Computer won the whole game with {p2.points} points!!!')



if __name__ == '__main__':
    main()
