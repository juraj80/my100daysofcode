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