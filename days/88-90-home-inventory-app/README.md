# Create a Home Inventory App

This is one of those "scratch your own itch" projects. Something we all need to do is properly track the contents of our homes for insurance purposes right? Here's an app to do it!

The app uses sqlite3 for the database and even has a generator thrown in for good measure!


## Day N: Watch videos and start planning!

Watch the first 3x videos detailing the *Main Menu*, *SQLite3 DB Access* and *Scrubbing Malicious Data* for your first day.

Start visualising how you'll form and write your app then get coding if you have time!


## Day N+1: App Run Through

Today we do a quick run through of the entire app. You'll see how all of the functions work together to form the final product.

Watch the *App Demonstration* video and start coding up your own solution if you haven't started already!


## Day N+2: Your Turn!

Watch the video *App Pitfalls and Bugs* and see if you're able to resolve the bugs!

These are all issues you'll need to take into account in your own app so it's worth giving it a try.

If you have even more time, see how you can expand this app to have its own GUI or web interface.


### Writing and working the main menu

....1,2,3,4,5 with the different options

```python
import sys

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
            add_inventory()
        elif choice == '3':
            view_inventory()
        elif choice == '4':
            calc_value()
        elif choice == '5':
            sys.exit()
        else:
            print("Invalid option, try again.")
```

In options 2 and 3 we need to check if a room exists in order to add an inventory and view its input. So we call 
function `check_input()` to check whether the room exists and if exists check its number:

```python
elif choice == '2':
    add_inventory(check_input())
elif choice == '3':
    view_inventory(check_input())


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
```
### SQLite3 database usage

```python
import sqlite3

conn = sqlite3.connect(DB)
cursor = conn.cursor()
cursor.execute("foo")
conn.commit()
conn.close()
```

We don't want to have this much of code in each function we want to connect to the DB. So we create a generator to wrap 
each function we want to connect to DB.

```python
import sqlite3
from contextlib import contextmanager

@contextmanager
def access_db():
    try:
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        yield cursor
    finally:
        conn.commit()
        conn.close()
```
and its use in a function:

```python
def list_rooms():
    room_list = []
    with access_db() as cursor:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        for room in cursor:
            room_list.append(room[0])
    return room_list
```

### Scrub function - SQLite3 workaround

Injecting of variable into a sql query is dangerous.

```python
def add_room():
    name = input("\nWhat name would you like to give the room? ")
    name = scrub(name)
    with access_db() as cursor:
        cursor.execute("CREATE TABLE '" + name.lower() + "' """"   
                        (Item TEXT, Value REAL)
                        """)
    print("\nA room with name %s has been added to the db. \n" % name)

def scrub(name):
    return ''.join( chr for chr in name if chr.isalnum() )

```

```python
>>> scrub('Juraj 99+/123?')
'Juraj99123'
```

Whole CLI with connection to DB:

```python
import sqlite3
import sys
from contextlib import contextmanager

DB = "Inventory.db"

#Script that creates the DB on first launch, otherwise is just a check.
def first_launch():
    try:
        conn = sqlite3.connect(DB)
    except:
        sys.exit('Error code X')

        
#generator to yield a db cursor and close the connection nicely.
@contextmanager
def access_db():
    try:
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        yield cursor
    finally:
        conn.commit()
        conn.close()


#A somewhat dirty menu. Improvement Point (make it a dict perhaps)
def main_menu():
    menu = {}
    menu['1'] = "Add Room."
    menu['2'] = "Add Inventory."
    menu['3'] = "View Inventory List."
    menu['4'] = "Total Value."
    menu['5'] = "Exit."
    while True:
        print("\n")
        for item, desc in sorted(menu.items()):
            print(item, desc)

        choice = input("Selection: ")
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


#Adds a room. Scrubs the input first to only allow default chars.
def add_room():
    name = input("\nWhat name would you like to give the room? ")
    name = scrub(name)
    with access_db() as cursor:
        cursor.execute("CREATE TABLE '" + name.lower() + "' """"
                                    (Item TEXT, Value REAL)
                                    """)
        print("\nA room with name %s has been added to the db.\n" % name)


#Parses the DB for table names and returns a list of the names.
def list_rooms():
    room_list = []
    with access_db() as cursor:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        for room in cursor:
            room_list.append(room[0])
    return room_list


#The scrubbing function. Removes all chars that aren't letters and numbers.
def scrub(table_name):
    return ''.join( chr for chr in table_name if chr.isalnum() )


#Checks the users' input to see if it matches a room/table name.
def check_input():
    while True:
        print('\n')
        for room in list_rooms():
            print(room)
        selection = input('Select a room: ').lower()
        if selection not in list_rooms():
            print("\n%s does not exist." % selection)
        else:
            return scrub(selection)


#Allows users to add an item and value to the DB of a specific room.
def add_inventory(selection):
    while True:
        name = input("\nName of item: ")
        cost = input("Monetary value: ")
        with access_db() as cursor:
            cursor.execute("INSERT INTO '" + selection + "' VALUES(?, ?)", [name, cost])

        cont = input('\nHit Q to quit or any other key to continue: ')
        if cont.lower() == 'q':
            break


#Returns a list of all items in a room and their total value.
def view_inventory(selection):
    total = 0
    with access_db() as cursor:
        cursor.execute("SELECT * FROM '" + selection + "'")
        print("\n")
        for data in cursor:
            print("%s: $%d" % (data[0], data[1]))
            total += data[1]
        print("Total Value: $%d" % total)


#Function to calculate the $ total of the entire database.
def calc_total():
    total = 0
    room_list = list_rooms()
    with access_db() as cursor:
        for room in room_list:
            cursor.execute("SELECT value FROM '" + room + "'")
            for value in cursor:
                total += value[0]
    print("\nTotal Value of all rooms: $%d" % total)


if __name__ == "__main__":
    first_launch()
    main_menu()

```
