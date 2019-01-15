from rolls import Roll, Player
import random

def main():
    print_header()
    rolls = build_the_three_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1,player2,rolls)



def print_header():
    print('-------------------------------')
    print('    Rock, Paper, Scissors')
    print('-------------------------------')


def get_players_name():
    name = input('Type your name here: ')
    return name

def build_the_three_rolls():
    Scissors = Roll('Scissors')
    Paper = Roll('Paper')
    Stone = Roll('Stone')
    return [Scissors,Paper,Stone]

def game_loop(p1,p2,rolls):
    count = 0

    while count < 3:
        p2_roll = random.choice(rolls) #TODO: get random roll

        p1_roll = input("Your choice? Enter [s]tone, [p]aper, or s[c]issors ? ").lower() #TODO: have player choose a roll
        if p1_roll == 's':
            p1_roll = rolls[2]
        elif p1_roll == 'p':
            p1_roll = rolls[1]
        elif p1_roll == 'c':
            p1_roll = rolls[0]
        else:
            print('Wrong input !!!')
            break

        print(f'Player {p1.name} throws {p1_roll.name}')
        print(f'Computer throws {p2_roll.name}')
#        outcome = p1_roll.can_defeat(p2_roll)

        # display throws
        # display winner for this round

        count += 1
    # Compute who won



if __name__ == '__main__':
    main()
