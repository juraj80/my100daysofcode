from actors import Creature,Wizard,Dragon
import random

def print_header():
    print('---------------------------------------')
    print('           WIZARD GAME APP')
    print('---------------------------------------')
    print()

def game_loop():

    creatures = [
        Creature('Bat', 5),
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Dragon('Dragon', 50, scaliness=2, breaths_fire=False),
        Wizard('Evil wizard', 1000),
    ]

    hero = Wizard('Gandolf', 75)

    while True:

        active_creature = random.choice(creatures)

        print(f'A {active_creature.name} of level {active_creature.level} has appear from a dark and foggy forest...')
        print()

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')

        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
                print(f'The wizard defeated {active_creature.name}')
            else:
                print(f'The wizard has been defeated by the powerful {active_creature.name}')
        elif cmd == 'r':
            print('The wizard has become unsure of his power and flees!!!')
        elif cmd == 'l':
            print('The wizard {} takes in the surroundings and sees:'.format(hero.name))
            for c in creatures:
                print(f'* {c.name} of level {c.level}')

        else:
            print("OK, exiting game... bye!")
            break

        if not creatures:
            print("You've  defeated all the cratures, well done!")
            break

    print()

def main():
    print_header()
    game_loop()


if __name__ == '__main__':
    main()