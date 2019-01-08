from unittest.mock import patch
import random
import pytest

from guess import get_random_number,Game

@patch.object(random, 'randint') # the module and the function we want to mock
def test_get_random_number(m):
    m.return_value = 17 # here we give it a fixed return value
    assert get_random_number() == 17

@patch("builtins.input", side_effects = [11,'12', 'bob',12,
                                         5, -1, 21, 7, None])
def test_guess(inp):
    game = Game()
    # good
    assert game.guess() == 11
    assert game.guess() == 12
    # not a number
    with pytest.raises(ValueError): # to ask pytest to check if it actually raises the exception to 'bob' input
        game.guess()
    # already guessed 12
    with pytest.raises(ValueError):
        game.guess()
    # good 5
    assert game.guess() == 5
    # out of range values
    with pytest.raises(ValueError):
        game.guess()
    with pytest.raises(ValueError):
        game.guess()
    # good 7
    assert game.guess() == 7
    # user hit enter
    with pytest.raises(ValueError):
        game.guess()

def test_validate_guess(capfd):
    game = Game()
    game._answer = 2

    assert not game._validate_guess(1)

