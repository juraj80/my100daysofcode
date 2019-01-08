## _py.test_

It's a popular testing framework, often preffered over the standard libraries unittest.

Serves for:
- validation of errors
- capturing standard output
- mocking certain functionality
- coverage how much of base code is covered by tests

http://docs.python-guide.org/en/latest/writing/tests/

Getting used to writing testing code and running this code in parallel is now considered a good habit. Used wisely, this method helps you define more precisely your code’s intent and have a more decoupled architecture.

Note: Importance of a regression test suite

Some general rules of testing:

- A testing unit should focus on one tiny bit of functionality and prove it correct.
- Each test unit must be fully independent. Each test must be able to run alone, and also within the test suite, regardless of the order that they are called. The implication of this rule is that each test must be loaded with a fresh dataset and may have to do some cleanup afterwards. This is usually handled by **setUp()** and **tearDown()** methods.
- Try hard to make tests that run fast. If one single test needs more than a few milliseconds to run, development will be slowed down or the tests will not be run as often as is desirable. In some cases, tests can’t be fast because they need a complex data structure to work on, and this data structure must be loaded every time the test runs. Keep these heavier tests in a separate test suite that is run by some scheduled task, and run all other tests as often as needed.
- Learn your tools and learn how to run a single test or a test case. Then, when developing a function inside a module, run this function’s tests frequently, ideally automatically when you save the code.
- Always run the full test suite before a coding session, and run it again after. This will give you more confidence that you did not break anything in the rest of the code.
- It is a good idea to implement a hook that runs all tests before pushing code to a shared repository.
- If you are in the middle of a development session and have to interrupt your work, it is a good idea to write a broken unit test about what you want to develop next. When coming back to work, you will have a pointer to where you were and get back on track faster.
- The first step when you are debugging your code is to write a new test pinpointing the bug. While it is not always possible to do, those bug catching tests are among the most valuable pieces of code in your project.
- Use long and descriptive names for testing functions. The style guide here is slightly different than that of running code, where short names are often preferred. The reason is testing functions are never called explicitly. square() or even sqr() is ok in running code, but in testing code you would have names such as test_square_of_number_2(), test_square_negative_number(). These function names are displayed when a test fails, and should be as descriptive as possible.
- When something goes wrong or has to be changed, and if your code has a good set of tests, you or other maintainers will rely largely on the testing suite to fix the problem or modify a given behavior. Therefore the testing code will be read as much as or even more than the running code. A unit test whose purpose is unclear is not very helpful in this case.
- Another use of the testing code is as an introduction to new developers. When someone will have to work on the code base, running and reading the related testing code is often the best thing that they can do to start. They will or should discover the hot spots, where most difficulties arise, and the corner cases. If they have to add some functionality, the first step should be to add a test to ensure that the new functionality is not already a working path that has not been plugged into the interface.

### Installation of pytest

1. Create and activate env

`python3 -m venv sample_env`
`source sample_env/bin/activate
`
2. Upgrade the version of pip

`pip install --upgrade pip
`
3. Install pytest and pytest-coverage

`pip install pytest pytest-cov
`

### unittest vs pytest

_hello.py_
```
def hello_name(name):
    return f'hello {name}'
```

_test_hello.py_
```    
import unittest

from hello import hello_name

class TestHello(unittest.TestCase):
    
    def test_hello_name(self):
        self.assertEqual(hello_name('bob'), 'hello bob')
        
if __name__ == '__main__':
    unittest.main()

```

Same test but with Pytest

_test_hello_pytest.py_
```
from hello import hello_name

def test_hello_name():
    assert hello_name('bob')== 'hello bob'
```

Then run it from command line:

`pytest test_hello_pytest.py
`

```
user$ pytest test_hello_pytest.py
===================================================================================== test session starts ======================================================================================
platform darwin -- Python 3.6.0, pytest-4.1.0, py-1.7.0, pluggy-0.8.0
rootdir: /hello_name, inifile:
plugins: cov-2.6.1
collected 1 item                                                                                                                                                                               

test_hello_pytest.py .                                                                                                                                                                   [100%]

=================================================================================== 1 passed in 0.03 seconds ===================================================================================

```

### Mocking randomness / pytest-cov

We use our guessing game script for testing. 

_guess.py_

```
import random

MAX_GUESSES = 5
START, END = 1, 20


def get_random_number():
    """Get a random number between START and END, returns int"""
    return random.randint(START, END)


class Game:
    """Number guess class, make it callable to initiate game"""

    def __init__(self):
        """Init _guesses, _answer, _win to set(), get_random_number(), False"""
        self._guesses = set()
        self._answer = get_random_number()
        self._win = False

    def guess(self):
        """Ask user for input, convert to int, raise ValueError outputting
           the following errors when applicable:
           'Please enter a number'
           'Should be a number'
           'Number not in range'
           'Already guessed'
           If all good, return the int"""
        guess = input(f'Guess a number between {START} and {END}: ')
        if not guess:
            raise ValueError('Please enter a number')

        try:
            guess = int(guess)
        except ValueError:
            raise ValueError('Should be a number')

        if guess not in range(START, END+1):
            raise ValueError('Number not in range')

        if guess in self._guesses:
            raise ValueError('Already guessed')

        self._guesses.add(guess)
        return guess

    def _validate_guess(self, guess):
        """Verify if guess is correct, print the following when applicable:
           {guess} is correct!
           {guess} is too high
           {guess} is too low
           Return a boolean"""
        if guess == self._answer:
            print(f'{guess} is correct!')
            return True
        else:
            high_or_low = 'low' if guess < self._answer else 'high'
            print(f'{guess} is too {high_or_low}')
            return False

    @property
    def num_guesses(self):
        return len(self._guesses)

    def __call__(self):
        """Entry point / game loop, use a loop break/continue,
           see the tests for the exact win/lose messaging"""
        while len(self._guesses) < MAX_GUESSES:
            try:
                guess = self.guess()
            except ValueError as ve:
                print(ve)
                continue

            win = self._validate_guess(guess)
            if win:
                guess_str = self.num_guesses == 1 and "guess" or "guesses"
                print(f'It took you {self.num_guesses} {guess_str}')
                self._win = True
                break
        else:
            # else on while/for = anti-pattern? do find it useful in this case!
            print(f'Guessed {MAX_GUESSES} times, answer was {self._answer}')


if __name__ == '__main__':
    game = Game()
    game()
```

How do we want to test it?
Ideally, we want to test one function or functionality in one pytest function. So let's start with the `get_random_number()`.

So we create a `test_guess.py` file where we import the actual program.

`from guess import get_random_number, Game
`
The first function get_random_number() uses a random integer from start to end and random returns to something randomly every time.
So how to test that? The way to do it in testing land is to mock an object and for this we are going to use the unittest patch method on the mock module.
In this function we are going to mock the random module.

```
from unittest.mock import patch
import random

@patch.object(random, 'randint') # the module and the function we want to patch
```
And then in our test function we can pass in an argument m and we can give that argument a fixed return value. And that is the key, because instead
of having random return something else every time we can give it a fixed value. So it's kind of an override of what randint() normally does. So now 
every time random gets called it gives us 17.

```
def test_get_random_number(m):
    m.return_value = 17 # here we give it a fixed return value
    assert get_random_number() == 17
```

_test_guess.py_
```
from unittest.mock import patch
import random

from guess import get_random_number,Game

@patch.object(random, 'randint') 
def test_get_random_number(m):
    m.return_value = 17 
    assert get_random_number() == 17

```
This show us how we can override certain things in our program we cannot really control.

Now we can run the test.

`(sample_env) MacBook-Pro-xxx:guess xxx$ pytest`

```
(sample_env) MacBook-Pro-uzivatela-xxx:guess xxx$ pytest
===================================================================================== test session starts ======================================================================================
platform darwin -- Python 3.6.0, pytest-4.1.0, py-1.7.0, pluggy-0.8.0
rootdir: /Users/guess, inifile:
plugins: cov-2.6.1
collected 1 item                                                                                                                                                                               

test_guess.py .                                                                                                                                                                          [100%]

=================================================================================== 1 passed in 0.03 seconds ===================================================================================

```

When we want to see how much coverage we have of our tests, we run this coverage command.

`pytest --cov-report term-missing --cov='.'`

```
(sample_env) MacBook-Pro-xxx:guess xxx$ pytest --cov-report term-missing --cov='.'
===================================================================================== test session starts ======================================================================================
platform darwin -- Python 3.6.0, pytest-4.1.0, py-1.7.0, pluggy-0.8.0
rootdir: /Users/guess, inifile:
plugins: cov-2.6.1
collected 1 item                                                                                                                                                                               

test_guess.py .                                                                                                                                                                          [100%]

---------- coverage: platform darwin, python 3.6.0-final-0 -----------
Name            Stmts   Miss  Cover   Missing
---------------------------------------------
guess.py           50     38    24%   17-19, 29-45, 53-59, 63, 68-83, 87-88
test_guess.py       6      0   100%
---------------------------------------------
TOTAL              56     38    32%


=================================================================================== 1 passed in 0.06 seconds ===================================================================================
```

### Mocking user input and exceptions

The second thing we want to test is the guess method.
```
 def guess(self):
        """Ask user for input, convert to int, raise ValueError outputting
           the following errors when applicable:
           'Please enter a number'
           'Should be a number'
           'Number not in range'
           'Already guessed'
           If all good, return the int"""
        guess = input(f'Guess a number between {START} and {END}: ')
        if not guess:
            raise ValueError('Please enter a number')

        try:
            guess = int(guess)
        except ValueError:
            raise ValueError('Should be a number')

        if guess not in range(START, END+1):
            raise ValueError('Number not in range')

        if guess in self._guesses:
            raise ValueError('Already guessed')

        self._guesses.add(guess)
        return guess
```

It takes a user input and input is not static, it can be random. Even worse, when we run this program, it could wait at the prompt to 
get input so our test would hang. Another thing is that we definitely don't want to use input literally in tests, so we are going to use
patch again and we are going to patch the builtins.input and this is another way of marking, where we can give it side_effects and a list
of expected returns in a row. Because we are having all these exceptions here, we're going to give it a bunch of inputs to go through all
these scenarios and see if each scenario throws the value error or accepts the guess as a correct one. And this will also show how we can
check for exceptions in pytest which are important because raising exceptions is a common Python pattern. So we are going to pass a sequence
of return values as if input was called that many times.
```
@patch("builtins.input", side_effects =[11,'12', 'bob',12, 
                                         5, -1, 21, 7, None])
```
After that we define test_guess function and we pass an argument, it can be anything. 

`def test_guess(inp):`

In function we create a game object and the constructor set defaults for all the internal variables. Then we can start to make assertions.
The first two side effects or returns are good.
```
def test_guess(inp):
    game = Game()
    # good
    assert game.guess() == 11
    assert game.guess() == 12
```

'12' as a string should be fine, because that can be converted into a int. The third, bob, is not a number and the way in pytest to check 
if an exception is raised is to use pytest.raises (we need to import that) and the name of the exception and than the statement that would 
trigger that exception. So the next return value from input in the row is bob string and if we call guess with that it should raise ValueError
and we are telling pytest to check if it actually raises that exception.
```
import pytest

def test_guess(inp):
    game = Game()
    # good
    assert game.guess() == 11
    assert game.guess() == 12
    # not a number
    with pytest.raises(ValueError):
        game.guess() 
```

And the same is true for the next one which is 12. If I guess again, the guess is already in the guesses set and the function manually raises a
ValueError.
```
def test_guess(inp):
    game = Game()
    ...
    # not a number ()
    with pytest.raises(ValueError):
        game.guess()
    # already guessed 12
    with pytest.raises(ValueError):
        game.guess()
```

5 should be fine

ValueError.

```
def test_guess(inp):
    game = Game()
    ...
    assert game.guess() == 5
    
```

-1 and 21 should raise an exception because both of them are out of range.
```
def test_guess(inp):
    game = Game()
    ...
    # out of range values
    with pytest.raises(ValueError):
        game.guess()
    with pytest.raises(ValueError):
        game.guess()
```
7 is good one 
```
def test_guess(inp):
    game = Game()
    ...
    # good
    assert game.guess() == 7    
```  

And finally None should not be a good one.

```
def test_guess(inp):
    game = Game()
    ...
    # user hit enter
    with pytest.raises(ValueError):
        game.guess()
```

So that is how we use mocking to circumvent this input function waiting for input and going through all these scenarios by giving various
side effects.


### Testing a program's stdout with capfd

Next function to test is _validate_guess(). We are going to use another feature of pytest, which is capfd - that will capture the standard
output of the program and execution. Very useful, because for this function we not only want to check for boolean return value, but we also 
want to see the actual output by the function to print and we want accurate information printed for the user:

Docstring:
```
"""Verify if guess is correct, print the following when applicable:
           {guess} is correct!
           {guess} is too high
           {guess} is too low
           Return a boolean"""
```
Capfd is very cool to capture output printed by our program.

`def test_validate_guess(capfd):`


So let's make a game and set the answer to 2.

```
def test_validate_guess(capfd):
    game = Game()
    game._answer = 2
```

Let's validate that 1 is not a winning number. The function should return False and to say False in pytest is to assert not some 
function is truthy.

`assert not game._validate_guess(1)`

And of course, is easy to do the same for higher assertion and finally for good assertion.
```
assert not game._validate_guess(3)
assert game._validate_guess(2)
```

And now back to capfd, if we actually want to see what the print is printing to the console, because that is what we see if we 
run the game and it's printing these kind of feedbacks to the user. So we want to test if these are what we are expecting.

