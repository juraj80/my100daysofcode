from unittest.mock import patch

import pytest
from program import get_players_name, get_player_roll, build_the_three_rolls, game_loop
from rolls import Roll, Player

@patch("builtins.input", side_effect=["Juraj", 123, None])
def test_get_players_name(inp):
    assert get_players_name() == "Juraj"
    assert get_players_name() == 123
    assert get_players_name() == None


paper = Roll('Paper')
assert isinstance(paper, Roll)

@patch("builtins.input",side_effect = ["p", "P","s", "S", "r", "R"])
def test_get_player_roll(inp):
     paper = get_player_roll()
     assert paper.name == "Paper"
     paper = get_player_roll()
     assert paper.name == "Paper"
     scissors = get_player_roll()
     assert scissors.name == "Scissors"
     scissors = get_player_roll()
     assert scissors.name == "Scissors"
     rock = get_player_roll()
     assert rock.name == "Rock"
     rock = get_player_roll()
     assert rock.name == "Rock"