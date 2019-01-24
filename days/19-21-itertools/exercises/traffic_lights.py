import itertools
import time
import random

colors = "red amber green".split()
rotation = itertools.cycle(colors)

def rg_timer():
    return random.randint(3,7)


def light_rotation(rotation=rotation):
    for color in rotation:
        if color == "amber":
            print("Caution! The light is %s" % color)
            time.sleep(3)
        elif color == "red":
            print("STOP! The light is %s" % color)
            time.sleep(rg_timer())
        else:
            print("Go! The light is %s" % color)
            time.sleep(rg_timer())

if __name__ == '__main__':
    light_rotation()
