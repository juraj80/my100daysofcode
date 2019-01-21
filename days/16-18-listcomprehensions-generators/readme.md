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

## Dictionary comprehensions

https://www.datacamp.com/community/tutorials/python-dictionary-comprehension

This is the general template you can follow for dictionary comprehension in Python:

`dict_variable = {key:value for (key,value) in dictonary.items()}
`
Dictionary comprehension is a powerful concept and can be used as:

- alternative to for loops
- alternative to lambda functions.

However, not all for loop can be written as a dictionary comprehension but all dictionary comprehension can be written with a for loop.

Lambda functions are a way of creating small anonymous functions. They are functions without a name. These functions are throw-away functions, which are only needed where they have been created. Lambda functions are mainly used in combination with the functions `filter()`, `map()` and `reduce()`.
```
# Initialize `fahrenheit` dictionary 
fahrenheit = {'t1':-30, 't2':-20, 't3':-10, 't4':0}

#Get the corresponding `celsius` values
celsius = list(map(lambda x: (float(5)/9)*(x-32), fahrenheit.values()))

#Create the `celsius` dictionary
celsius_dict = dict(zip(fahrenheit.keys(), celsius))

print(celsius_dict)
```

`{'t2': -28.88888888888889, 't3': -23.333333333333336, 't1': -34.44444444444444, 't4': -17.77777777777778}
`
Let's take a look at another situation, where you want to convert a dictionary of Fahrenheit temperatures into celsius.
Let's break the code down: first, you need to define a mathematical formula that does the conversion from Fahrenheit to Celsius. In the code, this is done with the help of the lambda function. You then pass this function as an argument to the `map()` function which then applies the operation to every item in the fahrenheit.values() list.
Remember the `values()` function? It returns a list containing the items stored in the dictionary.
What you have now is a list containing the temperature value in celsius, but the solution requires it to be a dictionary. Python has a built-in function called `zip()` which goes over the elements of iterators and aggregates them. You can read more about the `zip()` function here. In the example above, the zip function aggregates the item from `fahrenheit.keys()` and the celsius list, giving a key-value pair that you can put together in a dictionary using the `dict` function, which is the desired result.
Now, let's try to solve the same problem using dictionary comprehension:
```
# Initialize the `fahrenheit` dictionary 
fahrenheit = {'t1': -30,'t2': -20,'t3': -10,'t4': 0}

# Get the corresponding `celsius` values and create the new dictionary
celsius = {k:(float(5)/9)*(v-32) for (k,v) in fahrenheit.items()}

print(celsius_dict)
```

`{'t2': -28.88888888888889, 't3': -23.333333333333336, 't1': -34.44444444444444, 't4': -17.77777777777778}
`


## Generators - the basics
What is a Generator?

Well, there’s actually not much to it. A generator is just a function that generates values specifically when called with next(). Take this absolutely simple generator for example:
```
>>> def num_gen():
...     yield 1
...     yield 2
...     yield 3
... 
>>> 
>>> demo_gen = num_gen()
>>> next(demo_gen)
1
>>> next(demo_gen)
2
>>> next(demo_gen)
3
>>> next(demo_gen)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```
As you can see, we have a function num_gen() which uses yield to return the numbers 1, 2 and 3.

Normally you’d return these numbers via some sort of loop or with 3x print() functions which would print the numbers 1, 2 and 3 all at once.

With a generator however, the numbers are only returned when called using the next() function. Here’s what the code does:

We take num_gen() and assign it to a variable demo_gen to make this easier on us.

We use the next() function on demo_gen to request the “next” iteration of the demo_gen function. This results in the first yield only being returned.

Notice we then have to run next(demo_gen) two more times to see the next iteration in the code.

Once we’ve exhausted all of the yields within num_gen() running next() again results in a StopIteration error.

 _The StopIteration error appears because there are no more yield statements in the function. Calling next on the generator after this does not cause it to loop over and start again._


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
## List vs generator performance
```
import timeit
from datetime import datetime
import calendar

# Example
# mydata = 5
# def f1(x):
#     return x+1
# print(timeit.timeit("f1(mydata)", setup = "from __main__ import f1, mydata", number=1))


def timed(func):
    t0 = datetime.now()

    func()

    dt = datetime.now() - t0
    print("Time: {:,.3f} ms".format(dt.total_seconds() * 1000.0), flush=True)

# list
def leap_years_lst(n=1000000):
    leap_years = []
    for year in range(1, n+1):
        if calendar.isleap(year):
            leap_years.append(year)
    return leap_years

# generator
def leap_years_gen(n=1000000):
    for year in range(1, n+1):
        if calendar.isleap(year):

            yield year

timed(leap_years_lst)
print(timeit.timeit("leap_years_lst", setup = "from __main__ import leap_years_lst", number=1))

timed(leap_years_gen)
print(timeit.timeit("leap_years_gen", setup = "from __main__ import leap_years_gen", number=1))
```
## Generator Expressions

- General syntax

**(**_expression_ **for** i **in** s **if** _condition_**)**

- What it means
```
for i in s:
    if condition:
        yield expression
```

The parens on a generator expression can dropped if used as a single function argument


`sum(x*x for x in s)
`

## Generators as a Pipeline

The glue that holds the pipeline together is the iteration that occurs in each step
```
with open("access-log") as wwwlog:
    bytecolumn = (line.rsplit(None,1)[1] for line in wwwlog) 
    bytes_sent = (int(x) for x in bytecolumn if x != '-') 
    print("Total", sum(bytes_sent))
```
 The calculation is being driven by the last step.The **sum()** function is consuming values being pulled through the pipeline
 (via **__next__()** calls)

## Concept: List Comprehension and Generators

![alt text](pics/pic01.png)
   
![alt text](pics/pic02.png)

 
## Example for a list comprehension
```
import random

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

title_case =[name.title() for name in NAMES]
print(title_case)

def reverse_first_last_names(name):
    first,last = name.split()
    # ' '.join([last,first]) -- wait we have f-strings now (>= 3.6)
    return f'{last} {first}'

reversed = [reverse_first_last_names(name) for name in NAMES]

print(reversed)
```

## Example for a simple generator

```
def gen_pairs():
    first_names = [name.split()[0].title() for name in NAMES]
    while True:
        first,second = None, None
        while first == second:
            first, second = random.sample(first_names,2)
        yield f'{first} teams up with {second}'

pairs = gen_pairs()
for _ in range(10):
    print(next(pairs))
```
Another way to get a slice of a generator is using `itertools.islice`:
```
first_ten = itertools.islice(pairs,10)
list(first_ten)


def count(n):
    while True:
        yield n
        n+=1
        
c = count(0)
import itertools
for x in itertools.islice(c,10,20):
    print(x)
```

## Example for a generator pipeline

You have hundreds of web server logs scattered across various directories. In additional, some of the logs are compressed. 
Design a program so that you can easily read all of these logs.

```
foo/
 access-log-012007.gz
 access-log-022007.gz
    access-log-032007.gz
    ...
    access-log-012008
bar/
    access-log-092007.bz2
    ...
    access-log-022008
```
1. Search the filesystem with **Path.rglob()**

A useful way to search the filesystem:
```
from pathlib import Path

for filename in Path('/').rglob('*.py'):
    print(filename)
```
Guess what? It uses generators!
```
>>> from pathlib import Path
>>> Path('/').rglob('*.py')
<generator object Path.rglob at 0x10e3e0b88> 
>>>
```
So, we could build processing pipelines from it.

2. A File Opener

Open a sequence of paths:
```
import gzip, bz2
 def gen_open(paths):
     for path in paths:
         if path.suffix == '.gz':
              yield gzip.open(path, 'rt')
         elif path.suffix == '.bz2':
              yield bz2.open(path, 'rt')
         else:
              yield open(path, 'rt')
```
This is interesting...it takes a sequence of paths as input and yields a sequence of open file objects.

3. cat

Concatenate items from one or more source into a single sequence of items
```
def gen_cat(sources):
    for src in sources:
        for item in src:
            yield item
```            

OR

```
def gen_cat(sources):
    for src in sources:
        yield from src
```

Example:
```
lognames = Path('/usr/www').rglob("access-log*") # generate a generator
logfiles = gen_open(lognames)
loglines = gen_cat(logfiles)
```
## yield from

'yield from' can be used to delegate iteration:
```
def countdown(n):
    while n > 0:
        yield n
        n -= 1
        
def countup(stop):
    n = 1
    while n < stop:
        yield n
        n += 1
        
def up_and_down(n):
    yield from countup(n)
    yield from countdown(n)
    
for x in up_and_down(3):
    print(x)
    
1
2
3
2
1
    
``` 

4. grep

Generate a sequence of lines that contain a given regular expression. 
```
import re
def gen_grep(pat, lines):
   patc = re.compile(pat)
   return (line for line in lines if patc.search(line))
```
Example:
```
lognames = Path('/usr/www').rglob("access-log*") 
logfiles = gen_open(lognames)
loglines = gen_cat(logfiles)
patlines = gen_grep(pat, loglines)
```

Find out how many bytes transferred for a specific pattern in a whole directory of logs

```
pat = r"somepattern" 
logdir = "/some/dir/"

filenames  = Path(logdir).rglob("access-log*")
logfiles   = gen_open(filenames)
loglines   = gen_cat(logfiles)
patlines   = gen_grep(pat,loglines)
bytecolumn = (line.rsplit(None,1)[1] for line in patlines)
bytes_sent = (int(x) for x in bytecolumn if x != '-')
print("Total", sum(bytes_sent))
```