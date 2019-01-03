

from collections import namedtuple

user = ('juraj',38)

print(f'{user[0]} is {user[1]} years old')

User = namedtuple('User', 'name role')
user = User(name='bob',role='coder')

print(user.name)
print(user.role)


print(f'{user.name} is a {user.role}')

users = {'bob':'coder'}

users['bob']
# users['julian']

# Traceback (most recent call last):
#   File "/Users/jurajklucka/PycharmProjects/100daysOfCode/days/04-06-collections/examples.py", line 20, in <module>
#     users['julian']
# KeyError: 'julian'

print(users.get('bob'))