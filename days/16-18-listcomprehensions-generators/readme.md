## First day: list comprehensions and generators

```
names = 'pybites mike bob julian tim sara guido'.split()
names
['pybites', 'mike', 'bob', 'julian', 'tim', 'sara', 'guido']
for name in names:
    print(name.title())
    
Pybites
Mike
Bob
Julian
Tim
Sara
Guido

import string
first_half_alphabet = list(string.ascii_lowercase)[:13]
first_half_alphabet
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
new_names = []
for name in names:
    if name[0] in first_half_alphabet:
        new_names.append(name.title())
        
new_names
['Mike', 'Bob', 'Julian', 'Guido']
new_names2 = [name.title() for name in names if name[0] in first_half_alphabet]
new_names2
['Mike', 'Bob', 'Julian', 'Guido']
assert new_names == new_names2
```