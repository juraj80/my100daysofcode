from unittest.mock import patch
import random

from guess import get_random_number,Game

@patch.object(random, 'randint') # the module and the function we want to mock
def test_get_random_number(m):
    m.return_value = 17 # here we give it a fixed return value
    assert get_random_number() == 17

@patch("builtins.input"), side_effects =[11,'12', 'bob',12,
                                         5, -1, 21, 7, None]

