## Writing a simple list comprehension

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
## Cleaning data with list comprehensions

**regex:** \W matches any non-alphanumeric character;
this is equivalent to the set [^a-zA-Z0-9_]
```
import requests

resp = requests.get('http://projects.bobbelderbos.com/pcc/harry.txt')

words = resp.text.lower().split()
words[:5]
['the', 'boy', 'who', 'lived', 'mr.']

from collections import Counter
cnt = Counter(words)
cnt.most_common(5)
[('the', 202), ('he', 136), ('a', 108), ('and', 100), ('to', 93)]

'-' in words
True

import re
words = [re.sub(r'\W+',r'',word) for word in words]
```
**regex:** \W matches any non-alphanumeric character;
this is equivalent to the set [^a-zA-Z0-9_]

```
'-' in words
False

'the' in words
True

resp = requests.get('http://projects.bobbelderbos.com/pcc/stopwords.txt')
stopwords = resp.text.lower().split()
stopwords[:5]
['a', 'about', 'above', 'across', 'after']

words = [word for word in words if word.strip() and word not in stopwords]
words[:5]
['boy', 'lived', 'mr', 'mrs', 'dursley']

'the' in words
False

cnt = Counter(words)
cnt.most_common(5)
[('dursley', 45), ('dumbledore', 35), ('said', 32), ('mr', 30), ('professor', 30)]
```

### Generators - the basics
```
def num_gen():
    for n in range(10):
        yield n
        
gen = num_gen() # A generator is a function that returns an iterator.
next(gen)
0

for i in gen:
    print(i)
    
1
2
3
4
5
6
7
8
9

next(gen)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
StopIteration

gen = num_gen()
for i in gen:
    print(i)
    
0
1
2
3
4
5
6
7
8
9
```

## Use generators to build a sequence

pprint. pprint ( object, stream=None, indent=1, width=80, depth=None, *, compact=False )
Prints the formatted representation of object on stream, followed by a newline. If stream is None, sys.stdout is used. This may be used in the interactive interpreter instead of the print() function for inspecting values (you can even reassign print = pprint.pprint for use within a scope)

```
options = 'red yellow blue white black green purple'.split()
options
['red', 'yellow', 'blue', 'white', 'black', 'green', 'purple']


def create_select_options(options=options):
    select_list = []
    for option in options:
        select_list.append(f'<option value={option}>{option.title()}</option>')
    return select_list

from pprint import pprint as pp
```
pprint. pprint ( object, stream=None, indent=1, width=80, depth=None, *, compact=False )
Prints the formatted representation of object on stream, followed by a newline. If stream is None, sys.stdout is used. This may be used in the interactive interpreter instead of the print() function for inspecting values (you can even reassign print = pprint.pprint for use within a scope)

```
pp(create_select_options())
['<option value=red>Red</option>',
 '<option value=yellow>Yellow</option>',
 '<option value=blue>Blue</option>',
 '<option value=white>White</option>',
 '<option value=black>Black</option>',
 '<option value=green>Green</option>',
 '<option value=purple>Purple</option>']

def create_select_options_gen(options=options):
    for option in options:
        yield f'<option value={option}>{option.title()}</option>'
        
print(create_select_options_gen())
<generator object create_select_options_gen at 0x11080c938>

list(create_select_options_gen())
['<option value=red>Red</option>', '<option value=yellow>Yellow</option>', '<option value=blue>Blue</option>', '<option value=white>White</option>', '<option value=black>Black</option>', '<option value=green>Green</option>', '<option value=purple>Purple</option>']

```