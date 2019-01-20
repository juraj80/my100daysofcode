from bite26 import exclude_bites, filter_bites



def test_filter_bites():
    result = filter_bites()
    assert type(result) == dict
    assert len(result) == 10
    for bite in exclude_bites:
        assert bite not in result, f'Bite {bite} should not be in result'



