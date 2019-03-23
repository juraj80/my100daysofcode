import sqlite3
import sys
from contextlib import contextmanager

DB = "inventory.db"

def first_launch():
    try:
        conn = sqlite3.connect(DB)
    except:
        sys.exit('Error code X.')

@contextmanager
def access_db():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    yield cursor
    conn.commit()
    conn.close()

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
            calc_total()
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
        print(list_rooms())
        if selection not in list_rooms():
            print('\n%s does not exist.' % selection)
        else:
            return scrub(selection)

def add_room():
    name = input('Enter the name of new room: ')
    name = scrub(name)

    with access_db() as cursor:
        cursor.execute("CREATE TABLE'" + name.lower() + "'(Item TEXT, Value REAL)")

        print("\nRoom with name %s was added to the db." % name)

# def list_rooms():
#     return [room for room, items in ROOMS.items()]


def add_inventory(room):
    while True:
        print('\n')
        name = input('Enter the name of item: ')
        cost = float(input('Enter the value of item: '))
        with access_db() as cursor:
            cursor.execute("INSERT INTO '" + room + "' VALUES(?,?)", [name, cost])
            print(f"Item '{name}' with value {cost} added to the inventory of room {room}")

        cont = input('\nHit Q to quit or any other key to continue.')
        if cont.lower() == 'q':
            break


def view_inventory(room):
    print(f'Items or room {room} :')
    total = 0
    with access_db() as cursor:
        cursor.execute("SELECT * FROM '" + room + "'")
        for data in cursor:
            print("   %s: $%d" % (data[0], data[1]))
            total += data[1]
        print("Total value of room %s: $%d" % (room, total))

#Function to calculate the $ total of the entire database.
def calc_total():
    total = 0
    room_list = list_rooms()
    with access_db() as cursor:
        for room in room_list:
            cursor.execute("SELECT Value FROM '" + room + "'")
            for value in cursor:
                # print(value)
                total += value[0]
        print("Total value of all rooms: $%d" % total)


def list_rooms():
    room_list =[]
    with access_db() as cursor:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        for room in cursor:
            room_list.append(room[0])
    return room_list


def scrub(name):
    return ''.join( chr for chr in name if chr.isalnum())



if __name__ == '__main__':
    first_launch()
    main_menu()



