### Error handling

Standard Error handling template in Python:

```python
try:
    method1()
    method2()
    method3()
except ExceptionType1 as x:
    # details with x
except ExceptionType2 as x:
    # details with x
except Exception:
    # general error fallback.
finally:
    # code that runs regardless of error or success.
```

Starter code:

```python
import api


def main():
    keyword = input('Keyword of title search: ')
    results = api.find_movie_by_title(keyword)

    print(f'There are {len(results)} movies found.')
    for r in results:
        print(f"{r.title} with code {r.imdb_code} has score {r.imdb_score}")


if __name__ == '__main__':
    main()

```

Let's try to add the first try/except block.

```python
import api


def main():
    keyword = input('Keyword of title search: ')   
    try:
        results = api.find_movie_by_title(keyword)
    
        print(f'There are {len(results)} movies found.')
        for r in results:
            print(f"{r.title} with code {r.imdb_code} has score {r.imdb_score}")
    except:
        print("Oh that didn't work")

if __name__ == '__main__':
    main()

```

```python
import api
import requests.exceptions


def main():
    keyword = input('Keyword of title search: ')   
    try:
        results = api.find_movie_by_title(keyword)
    
        print(f'There are {len(results)} movies found.')
        for r in results:
            print(f"{r.title} with code {r.imdb_code} has score {r.imdb_score}")
    except requests.exceptions.ConnectionError:
        print("ERROR: Could not find server. Check your network connection")
    except:
        print("Oh that didn't work")

if __name__ == '__main__':
    main()

```
If we try to hit Enter as a Keyword of title search, it would return "Oh that didn't work". If we want to know details about
returned Exception we could change the except statement. What is the actual error?

```python
import api
import requests.exceptions


def main():
    keyword = input('Keyword of title search: ')
    try:
        results = api.find_movie_by_title(keyword)

        print(f'There are {len(results)} movies found.')
        for r in results:
            print(f"{r.title} with code {r.imdb_code} has score {r.imdb_score}")
    except requests.exceptions.ConnectionError:
        print("ERROR: Could not find server. Check your network connection")
    except Exception as x:
        print(type(x))
        print("Oh that didn't work: {}".format(x))


if __name__ == '__main__':
    main()
```

```
Keyword of title search:   # in case you hit Enter
<class 'ValueError'>
Oh that didn't work: Must specify a search term.

```
So it's a ValueError. So now let's add an exception clause for that.

```python
import api
import requests.exceptions


def main():
    keyword = input('Keyword of title search: ')
    try:
        results = api.find_movie_by_title(keyword)

        print(f'There are {len(results)} movies found.')
        for r in results:
            print(f"{r.title} with code {r.imdb_code} has score {r.imdb_score}")
    except requests.exceptions.ConnectionError:
        print("ERROR: Could not find server. Check your network connection")
    except ValueError:
        print("ERROR: You must specify a search term.")
    except Exception as x:
        print(type(x))
        print("Oh that didn't work: {}".format(x))

if __name__ == '__main__':
    main()
```
Now we can really tell the user what's going on.

```
Keyword of title search:   # in case you hit Enter
ERROR: You must specify a search term.

```

The final important thing to see here is the order in which we specify the errors. It's super important that this goes from most specific to most general.


### Concepts: Error handling and exceptions

![alt=text](pics/pic01.png)


Python has kind of an optimistic way of handling errors in compare to for example C. 
One of the key differentiators of professional programs and scripts thrown together by beginners is that the pro app does not crash. It anticipates all the error conditions and puts the proper error handling and user feedback to keep working. 
Ok, pro apps still crash, but they do so much less often. When they do, we have [logging](https://logbook.readthedocs.io) and other error monitoring such as [Rollbar](https://rollbar.com/?dr) so that we can get notified and fix these once we encounter them. This allows apps to grow stronger and more resilient over time.

Examples on exception types:
```
data = [1.0/i for i in range(1,10)]
data[9]
...
IndexError: list index out of range
```

```
C = float('21 C')
...
ValueError: could not convert string to float: '21 C'

```
```
print a
...
SyntaxError: Missing parentheses in call to 'print'
```

```
print (a)
...
NameError: name 'a' is not defined
```

```
3.0/0
...
ZeroDivisionError: float division by zero
```

```
'string' * 3.14
...
TypeError: can't multiply sequence by non-int of type 'float'
```

### Raising exceptions

Sometimes we see that an exception may happen, but if it happens, we want a more precise error message to help the user. This can be done by raising a new exception in an except block and provide the desired exception type and message.

Another application of raising exceptions with tailored error messages arises when input data are invalid. The code below illustrates how to raise exceptions in various cases.

```python
def read_C():
    try:
        C = float(sys.argv[1])
    except IndexError:
        raise IndexError\ 
        ('Celsius degrees must be supplied on the command line')
    except ValueError:
        raise ValueError\ 
        ('Celsius degrees must be a pure number, '\ 
        'not "%s"' % sys.argv[1])
    # C is read correctly as a number, but can have wrong value:
    if C < -273.15:
        raise ValueError('C=%g is a non-physical value!' % C)
    return C
```
Without raise:

```python
def f():
    try:
        x = int("four")
    except ValueError as e:
        print("Error in the function",e)
```
```
f()
Error in the function invalid literal for int() with base 10: 'four'
```

With raise:

```python
def f():
    try:
        x = int("four")
    except ValueError as e:
        print("Error in the function",e)
        raise
```

```

f()
Traceback (most recent call last):
Error in the function invalid literal for int() with base 10: 'four'
  File "<input>", line 1, in <module>
  File "<input>", line 3, in f
ValueError: invalid literal for int() with base 10: 'four'
```

Example: Reading an integer with input

```python
while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print("No valid integer! Please try again ...")
print("Great, you successfully entered an integer!")

```

It's a loop, which breaks only, if a valid integer has been given. 
The example script works like this:
The while loop is entered. The code within the try clause will be executed statement by statement. If no exception occurs during the execution, the execution will reach the break statement and the while loop will be left. If an exception occurs, i.e. in the casting of n, the rest of the try block will be skipped and the except clause will be executed. The raised error, in our case a ValueError, has to match one of the names after except. In our example only one, i.e. "ValueError:". After having printed the text of the print statement, the execution does another loop. It starts with a new input().

```
$ python integer_read.py 
Please enter an integer: abc
No valid integer! Please try again ...
Please enter an integer: 42.0
No valid integer! Please try again ...
Please enter an integer: 42
Great, you successfully entered an integer!
```

### Custom made exceptions
```
>>> raise SyntaxError("Sorry, my fault")

Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "<string>", line None
SyntaxError: Sorry, my fault
```
The best or the Pythonic way to do this, consists in defining an exception class which inherits from the Exception class.

```python
class MyException(Exception):
    pass

raise MyException("An exception doesn't always prove the rule!")
```

```
Traceback (most recent call last):
  File "<input>", line 1, in <module>
MyException: An exception doesn't always prove the rule!
```

### try - finally

"finally" clause is always executed regardless if an exception occurred in a try block or not. 
A simple example to demonstrate the finally clause:

```python
try:
    x = float(input("Your number: "))
    inverse = 1.0 / x
finally:
    print("There may or may not have been an exception.")
print("The inverse: ", inverse)
```

```
Your number: 34
There may or may not have been an exception.
```

### else Clause

The try ... except statement has an optional else clause. An else block has to be positioned after all the except clauses. An else clause will be executed if the try clause doesn't raise an exception. 

```python
import sys
file_name = sys.argv[1]
text = []
try:
    fh = open(file_name, 'r')
    text = fh.readlines()
    fh.close()
except IOError:
    print(f'No such file or directory: "{file_name}"')

if text:
    print(text[:100])

```

The previous example is nearly the same as:

```python
import sys
file_name = sys.argv[1]
text = []
try:
    fh = open(file_name, 'r')
except IOError:
    print(f'No such file or directory: "{file_name}"')
else:
    text = fh.readlines()
    fh.close()

if text:
    print(text[100])
```

The main difference is that in the first case, all statements of the try block can lead to the same error message "No such file ...", which is wrong, if fh.close() or fh.readlines() raise an error. 
