## Way of Selecting or filtering test Cases:
# 2-> Marking the test cases

import pytest

def func(x):
    if x%2==0:
        return x+5
    else:
        return x-5

@pytest.mark.chouhan
def test_case_by_Mohit():
    assert func(3) == -2

@pytest.mark.poddar
def test_case_by_Urmimala1():
    assert func(2) == 7

@pytest.mark.poddar
def test_case_by_Urmimala2():
    assert func(4) == 7

# -m is used to tell pytest that we are going to pass the name of the marker.