VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors():
    """Ask for color, lowercase it, check if 'quit' is entered, if so print
       'bye' and break, next check if given color is in VALID_COLORS, if not,
       continue, finally if that check passes, print the color"""
    while True:
        color = input('Enter a color: ')
        color = color.lower()
        if color == 'quit':
            print('bye')
            break
        elif color in VALID_COLORS:
            print(color)
        else:
            print('Not a valid color')
            continue

if __name__ == '__main__':
    print_colors()