
## First day: list comprehensions and generators

> List comprehensions and generators are in my top 5 favorite Python features leading to clean, robust and Pythonic code. 


```python
from collections import Counter
import calendar
import itertools
import random
import re
import string

import requests
```

### List comprehensions

Let's dive straight into a practical example. We all know how to use the classic for loop in Python, say I want to loop through a bunch of names title-casing each one:


```python
names = 'pybites mike bob julian tim sara guido'.split()
names
```




    ['pybites', 'mike', 'bob', 'julian', 'tim', 'sara', 'guido']




```python
for name in names:
    print(name.title())
```

    Pybites
    Mike
    Bob
    Julian
    Tim
    Sara
    Guido


Then I want to only keep the names that start with A-M, the `strings` module makes it easier (we love Python's standard library!):


```python
first_half_alphabet = list(string.ascii_lowercase)[:13]
first_half_alphabet
```




    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']




```python
new_names = []
for name in names:
    if name[0] in first_half_alphabet:
        new_names.append(name.title())
new_names
```




    ['Mike', 'Bob', 'Julian', 'Guido']



Feels verbose, not? 

If you don't know about list comprehensions you might start using them everywhere after seeing the next refactoring:


```python
new_names2 = [name.title() for name in names if name[0] in first_half_alphabet]
new_names2
```




    ['Mike', 'Bob', 'Julian', 'Guido']




```python
assert new_names == new_names2
```

From 4 to 1 lines of code, and it reads pretty well too. That's why we love and stick with Python! 

Here is another example I used recently to do a most common word count on Harry Potter. I used some list comprehensions to clean up the words before counting them:


```python
resp = requests.get('http://projects.bobbelderbos.com/pcc/harry.txt')
words = resp.text.lower().split()
words[:5]
```




    ['the', 'boy', 'who', 'lived', 'mr.']




```python
cnt = Counter(words)
cnt.most_common(5)
```




    [('the', 202), ('he', 136), ('a', 108), ('and', 100), ('to', 93)]



Hmm should not count stopwords, also:


```python
'-' in words
```




    True



Let's first clean up any non-alphabetic characters:


```python
words = [re.sub(r'\W+', r'', word) for word in words]
```


```python
'-' in words
```




    False




```python
'the' in words
```




    True



Ok let's filter those stopwords out plus the empty strings caussed by the previous list comprehension:


```python
resp = requests.get('http://projects.bobbelderbos.com/pcc/stopwords.txt')
stopwords = resp.text.lower().split()
stopwords[:5]  
```




    ['a', 'about', 'above', 'across', 'after']




```python
words = [word for word in words if word.strip() and word not in stopwords]
words[:5]
```




    ['boy', 'lived', 'mr', 'mrs', 'dursley']




```python
'the' in words
```




    False



Now it looks way better:


```python
cnt = Counter(words)
cnt.most_common(5)
```




    [('dursley', 45),
     ('dumbledore', 35),
     ('said', 32),
     ('mr', 30),
     ('professor', 30)]



What's interesting here is that the first bit of the list comprehension can be an expression like `re.sub`. The final bit can be a compound statement: here we checked for a non-empty word (' ' -> `strip()` -> '' = `False` in Python) `and` we checked `word not in stopwords`. 

Again, a lot is going on in one line of code, but the beauty of it is that it is totally fine, because it reads like plain English :)

### Generators

A generator is a function that returns an iterator. It generates values using the `yield` keyword, when called with next() (a for loop does this implicitly), and it raises a `StopIteration` exception when there are no more values to generate. Let's see what this means with a very simple example:


```python
def num_gen():
    for i in range(5):
        yield i
        
gen = num_gen()
```


```python
next(gen)
```




    0




```python
# note it takes off where we left it last statement
for i in gen:
    print(i)
```

    1
    2
    3
    4



```python
# no more values to generate
next(gen)
```


    ---------------------------------------------------------------------------

    StopIteration                             Traceback (most recent call last)

    <ipython-input-21-63d934b06ce9> in <module>()
          1 # no more values to generate
    ----> 2 next(gen)
    

    StopIteration: 



```python
# for catches the exception for us
for i in gen:
    print(i)
```

> The `StopIteration` error appears because there are no more yield statements in the function. Calling next on the generator after this does not cause it to loop over and start again. - [Generators are Awesome, Learning by Example
](https://pybit.es/generators.html)




Since learning about generators, a common pattern I use is to build up my sequences:


```python
options = 'red yellow blue white black green purple'.split()
options
```




    ['red', 'yellow', 'blue', 'white', 'black', 'green', 'purple']



My older code:


```python
def create_select_options(options=options):
    select_list = []
    
    for option in options:
        select_list.append(f'<option value={option}>{option.title()}</option>')
    
    return select_list
```


```python
from pprint import pprint as pp
pp(create_select_options())
```

    ['<option value=red>Red</option>',
     '<option value=yellow>Yellow</option>',
     '<option value=blue>Blue</option>',
     '<option value=white>White</option>',
     '<option value=black>Black</option>',
     '<option value=green>Green</option>',
     '<option value=purple>Purple</option>']


Using a generator you can write this in 2 lines of code - my newer code:


```python
def create_select_options_gen(options=options):    
    for option in options:
        yield f'<option value={option}>{option.title()}</option>'
```


```python
print(create_select_options_gen())
```

    <generator object create_select_options_gen at 0x10afca570>


Note that generators are _lazy_ so you need to explicitly consume them by iterating over them, for example by looping over them. Another way is to pass them into the `list()` constructor:


```python
list(create_select_options_gen())
```




    ['<option value=red>Red</option>',
     '<option value=yellow>Yellow</option>',
     '<option value=blue>Blue</option>',
     '<option value=white>White</option>',
     '<option value=black>Black</option>',
     '<option value=green>Green</option>',
     '<option value=purple>Purple</option>']



Specially when working with large data sets you definitely want to use generators. Lists can only get as big as they fit memory size. Generators are lazily evaluated meaning that they only hold a certain amount of data in memory at once. Just for the sake of giving Python something to do, let's calculate leap years for a million years, and compare performance of list vs generator:


```python
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
```

PRO  tip: [since Python 3.3](https://docs.python.org/3/whatsnew/3.3.html) you can use the `yield from` syntax.


```python
# this had me waiting for a few seconds
%timeit -n1 leap_years_lst()
```

    396 ms ± 14.9 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)



```python
# this was instant
%timeit -n1 leap_years_gen()
```

    The slowest run took 4.72 times longer than the fastest. This could mean that an intermediate result is being cached.
    870 ns ± 682 ns per loop (mean ± std. dev. of 7 runs, 1 loop each)


That is pretty impressive. This is an important concept to know about because Big Data is here to stay!

## Second day: practice

Look at your code and see if you can refactor it to use list comprehensions. Same for generators. Are you building up a list somewhere where you could potentially use a generator?

And/or exercise here, take this list of names:


```python
NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']
```

Can you write a simple list comprehension to convert these names to title case (brad pitt -> Brad Pitt). Or reverse the first and last name? 

Then use this same list and make a little generator, for example to randomly return a pair of names, try to make this work:

    pairs = gen_pairs()
    for _ in range(10):
        next(pairs)

Should print (values might change as random):

    Arnold teams up with Brad
    Alec teams up with Julian

Have fun!

## Third day: solution / simulate unix pipelines

I hope yesterday's exercise was reasonably doable for you. Here are the answers in case you got stuck:


```python
# list comprehension to title case names
[name.title() for name in NAMES]
```




    ['Arnold Schwarzenegger',
     'Alec Baldwin',
     'Bob Belderbos',
     'Julian Sequeira',
     'Sandra Bullock',
     'Keanu Reeves',
     'Julbob Pybites',
     'Bob Belderbos',
     'Julian Sequeira',
     'Al Pacino',
     'Brad Pitt',
     'Matt Damon',
     'Brad Pitt']




```python
# list comprehension to reverse first and last names
# using a helper here to show you that list comprehensions can be passed in functions!

def reverse_first_last_names(name):
    first, last = name.split()
    # ' '.join([last, first]) -- wait we have f-strings now (>= 3.6)
    return f'{last} {first}'

[reverse_first_last_names(name) for name in NAMES]
```




    ['schwarzenegger arnold',
     'baldwin alec',
     'belderbos bob',
     'sequeira julian',
     'bullock sandra',
     'reeves keanu',
     'pybites julbob',
     'belderbos bob',
     'sequeira julian',
     'pacino al',
     'pitt brad',
     'damon matt',
     'pitt brad']




```python
def gen_pairs():
    # again a list comprehension is great here to get the first names
    # and title case them in just 1 line of code (this comment took 2)
    first_names = [name.split()[0].title() for name in NAMES]
    while True:
        
        # added this when I saw Julian teaming up with Julian (always test your code!)
        first, second = None, None
        while first == second: 
            first, second = random.sample(first_names, 2)
        
        yield f'{first} teams up with {second}'
```


```python
pairs = gen_pairs()
for _ in range(10):
    print(next(pairs))
```

    Alec teams up with Julbob
    Keanu teams up with Bob
    Keanu teams up with Julbob
    Julian teams up with Arnold
    Bob teams up with Alec
    Matt teams up with Alec
    Julbob teams up with Brad
    Julian teams up with Alec
    Julian teams up with Julbob
    Julbob teams up with Julian


Another way to get a slice of a generator is using `itertools.islice`:


```python
first_ten = itertools.islice(pairs, 10)
first_ten
```




    <itertools.islice at 0x10b1002c8>




```python
list(first_ten)
```




    ['Sandra teams up with Julian',
     'Matt teams up with Julian',
     'Al teams up with Julian',
     'Brad teams up with Julian',
     'Alec teams up with Arnold',
     'Matt teams up with Bob',
     'Matt teams up with Julian',
     'Julbob teams up with Julian',
     'Brad teams up with Julian',
     'Julian teams up with Julbob']



### Further practice

Read up on set and dict comprehensions, then try these two Bites:
- [Bite 5. Parse a list of names](https://codechalleng.es/bites/5/) (use a set comprehension in first function)
- [Bite 26. Dictionary comprehensions are awesome](https://codechalleng.es/bites/promo/awesome-dict-comprehensions)

Here is a more advanced generators exercise you can try: [Code Challenge 11 - Generators for Fun and Profit](https://codechalleng.es/challenges/11/)

### Time to share what you've accomplished!

Be sure to share your last couple of days work on Twitter or Facebook. Use the hashtag **#100DaysOfCode**. 

Here are [some examples](https://twitter.com/search?q=%23100DaysOfCode) to inspire you. Consider including [@talkpython](https://twitter.com/talkpython) and [@pybites](https://twitter.com/pybites) in your tweets.

*See a mistake in these instructions? Please [submit a new issue](https://github.com/talkpython/100daysofcode-with-python-course/issues) or fix it and [submit a PR](https://github.com/talkpython/100daysofcode-with-python-course/pulls).*
