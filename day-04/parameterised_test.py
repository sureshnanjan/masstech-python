import pytest


@pytest.mark.parametrize("arg1",[1,5,10,15])
def test_taking_arguments(arg1):
    assert arg1 > 10, "Passes if value greater than 10"
