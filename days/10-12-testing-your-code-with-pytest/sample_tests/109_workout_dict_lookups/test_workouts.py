from workouts import get_workout_motd,workout_schedule, rest, chill, go_train
import pytest

@pytest.mark.parametrize("arg, expected", [
    ('Monday', 'Go train Chest+biceps'),
    ('Tuesday', 'Go train Back+triceps'),
    ('Wednesday', 'Go train Core'),
    ('Thursday', 'Go train Legs'),
    ('Friday', 'Go train Shoulders'),
    ('Saturday', 'Chill out!'),
    ('Sunday', 'Chill out!'),
])

def test_get_workout_valid_case_insensitive_dict_lookups(arg,expected):
   mixed_case = arg[:3].lower() + arg[3:].upper()
   for day in (arg,arg.upper(),arg.lower(), mixed_case):
       assert get_workout_motd(day) == expected



def test_get_workout_invalid_dict_lookups_raise_exception():
    with pytest.raises(KeyError):
        get_workout_motd('not a day')









