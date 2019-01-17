from unittest.mock import patch
import random
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

@patch("builtins.input",side_effect = ["p", "P","s", "S", "r", "R",'t'])
def test_get_player_roll(inp,capfd):
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
     reply = get_player_roll()
     assert reply == None
     out, _ = capfd.readouterr()
     assert out.rstrip() == 'Wrong Input'

@patch("builtins.input",side_effect = ["p","s","r"])
def test_game_loop(inp,capfd):
    player1 = Player("Admin", 0)
    player2 = Player("System", 0)

    rolls = build_the_three_rolls()
    assert len(rolls) == 3

    p1_roll = Roll("Scissors")
    p2_roll = Roll("Paper")
    assert p1_roll.can_defeat(p2_roll)

    p1_roll = Roll("Paper")
    p2_roll = Roll("Scissors")
    assert not p1_roll.can_defeat(p2_roll)

    p1_roll = Roll("Rock")
    p2_roll = Roll("Scissors")
    assert p1_roll.can_defeat(p2_roll)

    p1_roll = Roll("Scissors")
    p2_roll = Roll("Rock")
    assert not p1_roll.can_defeat(p2_roll)

    p1_roll = Roll("Paper")
    p2_roll = Roll("Rock")
    assert p1_roll.can_defeat(p2_roll)

    p1_roll = Roll("Rock")
    p2_roll = Roll("Paper")
    assert not p1_roll.can_defeat(p2_roll)

    game_loop(player1,player2,rolls)
    out, _ = capfd.readouterr()
    print(out)
#
# @patch.object(random, 'randint') # the module and the function we want to mock
# def test_get_random_number(m):
#     m.return_value = 17 # here we give it a fixed return value
#     assert get_random_number() == 17
#
#
#
#
