import sys

ROOMS = {}

def main_menu():
    menu = {}
    menu['1'] = "Add Room."
    menu['2'] = "Add Inventory."
    menu['3'] = "View Inventory List."
    menu['4'] = "Total Value."
    menu['5'] = "Exit."

    while True:
        print('\n')
        for num,item in sorted(menu.items()):
            print(num,item)

        choice = input('Selection: ')
        if choice == '1':
            add_room()
        elif choice == '2':
            add_inventory(check_input())
        elif choice == '3':
            view_inventory(check_input())
        elif choice == '4':
            calc_value(check_input())
        elif choice == '5':
            sys.exit()
        else:
            print("Invalid option, try again.")

def check_input():
    while True:
        print('\n')
        for room in list_rooms():
            print(room)
        selection = input('Select a room: ').lower()
        if selection not in list_rooms():
            print('\n%s does not exist.' % selection)
        else:
            return selection

def add_room():
    name = input('Enter the name of new room: ').lower()
    ROOMS[name] = {}
    print(f"Room '{name}' added.")

def list_rooms():
    return [room for room, items in ROOMS.items()]


def add_inventory(room):
    item = input('Enter the name of item: ')
    value = float(input('Enter the value of item: '))
    ROOMS[room].update({item: value})
    print(f"Item '{item}' with value {value} added to the inventory of room {room}")

def view_inventory(room):
    print(f'Items or room {room} :')
    # print(ROOMS[room])
    # print(type(ROOMS[room]))
    for item, value in ROOMS[room].items():
        print('item: %s, Value: %f' % (item, value))

def calc_value(room):
    total = 0
    for item, value in ROOMS[room].items():
        total += value
    print(f'Total value of room {room} is {total} ')


if __name__ == '__main__':
    main_menu()



