from colors import print_colors
import pytest
from unittest.mock import patch

@patch("builtins.input", side_effect = ['green','Orange','Blue', 'Yellow', 'quit'])

def test_print_colors(inp, capfd):
    not_valid = 'Not a valid color'
    expected = '\n'.join([not_valid,not_valid,'blue','yellow', 'bye'])
    print_colors()
    out = capfd.readouterr()[0].strip()
    assert out == expected
