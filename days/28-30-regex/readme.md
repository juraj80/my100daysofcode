
# Regular Expressions in Python

> Some people, when confronted with a problem, think, "I know, I'll use regular expressions." Now they have two problems. - Jamie Zawinski


https://docs.python.org/3.6/howto/regex.html
https://docs.python.org/3.6/library/re.html

Write some regexes interactively using an online tool like regex101.

https://regex101.com/#python


## First day: quick overview

This first day we will explore the basics of the `re` (standard libary) module so you can start adding this powerful skill to your Python toolkit.


```python
import re
```

### When not to use regexes? 

Basically when regular string manipulations will do, for example:


```python
text = 'Awesome, I am doing the #100DaysOfCode challenge'
```

Does text start with 'Awesome'?


```python
text.startswith('Awesome')
```
```
True
```


Does text end with 'challenge'?


```python
text.endswith('challenge')
```
```
True
```

Does text contain '100daysofcode' (case insensitive)



```python
'100daysofcode' in text.lower()
```
```
True
```

I am bold and want do do 200 days (note strings are inmutable, so save to a new string)


```python
text.replace('100', '200')
```
```
'Awesome, I am doing the #200DaysOfCode challenge'
```

### Regex == Meta language

But what if you need to do some more tricky things, say matching any #(int)DaysOfCode? Here you want to use a regex pattern. Regular expressions are a (meta) language on their own and I highly encourage you to read through [this HOWTO](https://docs.python.org/3.7/howto/regex.html#regex-howto) to become familiar with their syntax.

### `search` vs `match` 

The main methods you want to know about are `search` and `match`, former matches a substring, latter matches the string from beginning to end. I always embed my regex in `r''` to avoid having to escape special characters like \d (digit), \w (char), \s (space), \S (non-space), etc (I think \\\d and \\\s clutters up the regex)

Note: 
 - match() checks at the start of a string and returns None if nothing is found.
 - search() moves up the string, looking for the first occurrence of the given pattern, and returns None only if the pattern occurs nowhere in the string.

```python
text = 'Awesome, I am doing the #100DaysOfCode challenge'
```


```python
re.search(r'I am', text)
```
```
<_sre.SRE_Match object; span=(9, 13), match='I am'>
```

```python
re.match(r'I am', text)
```
```

```

```python
re.match(r'Awesome.*challenge', text)
```

```
<_sre.SRE_Match object; span=(0, 48), match='Awesome, I am doing the #100DaysOfCode challenge'>

```

### Capturing strings

A common task is to retrieve a match, you can use _capturing () parenthesis_ for that:


```python
hundred = 'Awesome, I am doing the #100DaysOfCode challenge'
two_hundred = 'Awesome, I am doing the #200DaysOfCode challenge'

m = re.match(r'.*(#\d+DaysOfCode).*', hundred)
m.groups()
```
```
('#100DaysOfCode',)
```
```python
m.groups()[0]
```
```
'#100DaysOfCode'
```

```python
m = re.search(r'(#\d+DaysOfCode)', two_hundred)
m.groups()[0]
```
```
'#200DaysOfCode'
```

Note:

- () capturing group - the regex inside the parenthesis must be matched and the match create a capturing group
- (?:) non capturing group - the regex inside the parenthesis must be matched but doesn't not create the capturing group

####Non-capturing parenthesis

Use (?: ) to not capture matching contents, for example lets get all links and hashtags out of the tweet below. I need the outer parenthesis for capturing and the inner parenthesis to say '# or http', latter should not capture anything:
```python
tweet = 'New PyBites article: Module of the Week - Requests-cache for Repeated API Calls - http://pybit.es/requests-cache.html … #python #APIs'
re.findall(r'((?:#|http)\S+)',tweet)
```
```
['http://pybit.es/requests-cache.html', '#python', '#APIs']
```
When I don't use (?: ) it goes wrong:

```python
re.findall(r'((#|http)\S+)',tweet)
```
```
[('http://pybit.es/requests-cache.html', 'http'), ('#python', '#'), ('#APIs', '#')]
```
The required result without non-capturing parenthesis we would get if we use also this regex:

```python
re.findall(r'#\S+|http\S+',tweet)
```
```
['http://pybit.es/requests-cache.html', '#python', '#APIs']
```

### `findall` is your friend

What if you want to match multiple instances of a pattern? `re` has the convenient `findall` method I use a lot. For example in [our 100 Days Of Code](https://github.com/pybites/100DaysOfCode/blob/master/LOG.md) we used the `re` module for the following days - how would I extract the days from this string?


```python
text = '''
$ python module_index.py |grep ^re
re                 | stdlib | 005, 007, 009, 015, 021, 022, 068, 080, 081, 086, 095
'''

re.findall(r'\d+', text)
```

```
['005', '007', '009', '015', '021', '022', '068', '080', '081', '086', '095']
```

How cool is that?! Just because we can, look at how you can find the most common word combining `findall` with `Counter`:


```python
text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been 
the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and 
scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus
PageMaker including versions of Lorem Ipsum"""
```

```python
text.split()[:5]
```

```
['Lorem', 'Ipsum', 'is', 'simply', 'dummy']
```

Of course you can do the same with `words.split()` but if you have more requirements you might fit it in the same regex, for example let's only count words that start with a capital letter.

I am using two _character classes_ here (= pattern inside `[]`), the first to match a capital letter, the second to match 0 or more common word characters. 

Note I am escaping the single quote (') inside the second character class, because the regex pattern is wrapped inside single quotes as well: 


```python
from collections import Counter

cnt = Counter(re.findall(r'[A-Z][A-Za-z0-9\']*', text))
cnt.most_common(5)
```
```
[('Lorem', 4), ('Ipsum', 4), ('It', 2), ('Letraset', 1), ('Aldus', 1)]
```
### Regexes are greedy!

Take this modified html:
```python
html = """<div><p>Today a quick article on a nice caching module when working with APIs.</p><p>Read more ...</p></div>"""
```
Imagine we want to match the first paragraph:

```python
m = re.search('<p>.*</p>', html)
m.group()
```
Oops, it matched too much:
```
'<p>Today a quick article on a nice caching module when working with APIs.</p><p>Read more ...</p>'

```
You can prevent this default greediness by using the ? after the repeating metacharacter (*, +, etc) which makes it match as little text as possible:

```python
m = re.search('<p>.*?</p>', html)
m.group()
```
```
'<p>Today a quick article on a nice caching module when working with APIs.</p>'
```


### Compiling regexes

If you want to run the same regex multiple times, say in a for loop it is best practice to define the regex one time using `re.compile`, here is an example:


```python
movies = '''1. Citizen Kane (1941)
2. The Godfather (1972)
3. Casablanca (1942)
4. Raging Bull (1980)
5. Singin' in the Rain (1952)
6. Gone with the Wind (1939)
7. Lawrence of Arabia (1962)
8. Schindler's List (1993)
9. Vertigo (1958)
10. The Wizard of Oz (1939)'''.split('\n')
movies
```

Let's find movie titles that have exactly 2 words, just for exercise sake. Before peaking to the solution how would _you_ define such a regex?
```python
for movie in movies:
    lst = re.findall(r'[A-Za-z\']+\s',movie)
    if len(lst) == 2:
        print(lst)
```
```
['Citizen', 'Kane']
['The', 'Godfather']
['Raging', 'Bull']
["Schindler's ", 'List ']

```



OK here is another way to do it, I am using `re.VERBOSE` which ignores spaces and comments so I can explain what each part of the regex does (really nice!):


```python
pat = re.compile(r'''
                  ^             # start of string
                  \d+           # one or more digits
                  \.            # a literal dot
                  \s+           # one or more spaces
                  (?:           # non-capturing parenthesis, so I don't want store this match in groups()
                  [A-Za-z']+\s  # character class (note inclusion of ' for "Schindler's"), followed by a space
                  )             # closing of non-capturing parenthesis
                  {2}           # exactly 2 of the previously grouped subpattern
                  \(            # literal opening parenthesis
                  \d{4}         # exactly 4 digits (year)
                  \)            # literal closing parenthesis
                  $             # end of string
                  ''', re.VERBOSE)
```

As we've seen before if the regex matches it returns an `_sre.SRE_Match` object, otherwise it returns `None`


```python
for movie in movies:
    print(movie, pat.match(movie))
```

```
1. Citizen Kane (1941) <_sre.SRE_Match object; span=(0, 22), match='1. Citizen Kane (1941)'>
2. The Godfather (1972) <_sre.SRE_Match object; span=(0, 23), match='2. The Godfather (1972)'>
3. Casablanca (1942) None
4. Raging Bull (1980) <_sre.SRE_Match object; span=(0, 21), match='4. Raging Bull (1980)'>
5. Singin' in the Rain (1952) None
6. Gone with the Wind (1939) None
7. Lawrence of Arabia (1962) None
8. Schindler's List (1993) <_sre.SRE_Match object; span=(0, 26), match="8. Schindler's List (1993)">
9. Vertigo (1958) None
10. The Wizard of Oz (1939) None

```

### Advanced string replacing

As shown before `str.replace` probably covers a lot of your needs, for more advanced usage there is `re.sub`: 


```python
text = '''Awesome, I am doing #100DaysOfCode, #200DaysOfDjango and of course #365DaysOfPyBites'''

# I want all challenges to be 100 days, I need a break!
text.replace('200', '100').replace('365', '100')
```
```
'Awesome, I am doing #100DaysOfCode, #100DaysOfDjango and of course #100DaysOfPyBites'
```


`re.sub` makes this easy:


```python
re.sub(r'\d+', '30', text)
```
```
'Awesome, I am doing #30DaysOfCode, #30DaysOfDjango and of course #30DaysOfPyBites'
```


Or what if I want to change all the #nDaysOf... to #nDaysOfPyton? You can use `re.sub` for this. Note how I use the capturing parenthesis to port over the matching part of the string to the replacement (2nd argument) where I use `\1` to reference it:


```python
re.sub(r'(#\d+DaysOf)\w+', r'\1Python', text)
```

```
'Awesome, I am doing #100DaysOfPython, #200DaysOfPython and of course #365DaysOfPython'
```


And that's a wrap. I only showed you some of the common `re` features I use day-to-day, but there is much more. I hope you got a taste for writing regexes in Python.

## Second day: solidify what you've learned

A. We recommend reading [10 Tips to Get More out of Your Regexes](https://pybit.es/mastering-regex.html) + watching the Al Sweigart's PyCon talk: _Yes, It's Time to Learn Regular Expressions_, linked at the end. 

If you still have time check out [the mentioned HOWTO](https://docs.python.org/3.7/howto/regex.html#regex-howto) and the [docs](https://docs.python.org/3.7/library/re.html).

B. Write some regexes interactively using an online tool like [regex101](https://regex101.com/#python).


## Third day: put your new skill to the test!

A. Take [Bite 2. Regex Fun](https://codechalleng.es/bites/2/) which should be within reach after studying the materials. It let's you write 3 regexes. Like to work on your desktop? Maybe you can do [blog challenge 42 - Mastering Regular Expressions](https://codechalleng.es/challenges/42/) which is similar but let's you solve 6 regex problems!

B. More fun: `wget` or `request.get` your favorite site and use regex on the output to parse out data (fun trivia: a similar exercise is where [our code challenges started](https://pybit.es/js_time_scraper_ch.html)).

Good luck and remember: 

> Keep calm and code in Python

### Time to share what you've accomplished!

Be sure to share your last couple of days work on Twitter or Facebook. Use the hashtag **#100DaysOfCode**. 

Here are [some examples](https://twitter.com/search?q=%23100DaysOfCode) to inspire you. Consider including [@talkpython](https://twitter.com/talkpython) and [@pybites](https://twitter.com/pybites) in your tweets.

*See a mistake in these instructions? Please [submit a new issue](https://github.com/talkpython/100daysofcode-with-python-course/issues) or fix it and [submit a PR](https://github.com/talkpython/100daysofcode-with-python-course/pulls).*
