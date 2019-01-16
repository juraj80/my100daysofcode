from rolls import  Roll, Player
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

def get_player_roll():
    inp = input("Choose [r]ock, [p]aper, or [s]cissors: ").lower()
    if inp == 'r':
        return Roll('Rock')
    elif inp == 'p':
        return Roll('Paper')
    elif inp == 's':
        return Roll('Scissors')
    else:
        print('Wrong Input')
        return get_player_roll()


def build_the_three_rolls():
    scissors = Roll('Scissors')
    paper = Roll('Paper')
    rock = Roll('Rock')
    return [scissors,paper,rock]

def game_loop(p1,p2,rolls):
    count = 0
    print(f"Thank you {p1.name}, let's play a game Rock, Paper, Scissors!!! ")
    print()

    while count < 3:
        p2_roll = random.choice(rolls)

        p1_roll = get_player_roll()
        print(f'{p1.name} throws {p1_roll.name}')
        print(f'Computer throws {p2_roll.name}')


        if p2_roll.name == p1_roll.name:
            print("It's a Tie. One more try!")
            continue

        # display throws

        print()
        outcome = p1_roll.can_defeat(p2_roll)
        # display winner for this round

        if outcome:
            p1.points+=1
            print(f'{p1.name} wins round {count+1} with {p1_roll.name} and have {p1.points} points')
        else:
            p2.points+=1
            print(f'Computer wins round {count+1} with {p2_roll.name} and have {p2.points} points')

        count += 1
        print()

    # display winner for this round
    if p1.points == 0 and p2.points == 0:
        print('Game finished with the draw. ')
    elif p1.points > p2.points:
        print(f'{p1.name} won the whole game with score {p1.points}:{p2.points}!!!')
    else:
        print(f'Computer won the whole game with {p2.points}:{p1.points}!!!')


if __name__ == '__main__':
    main()
