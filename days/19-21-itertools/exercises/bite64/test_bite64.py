from bite64 import get_attendees



def test_get_attendes(capfd):
    get_attendees()
    output = capfd.readouterr()[0].strip().split('\n')

    assert len(output) == 8
    assert "('Kim', '-', '-')" in output
    assert "('Andre', '-', '-')" in output
