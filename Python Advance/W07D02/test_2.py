## Way of Selecting or filtering test Cases:
# 1-> Runnning the test cases with substring matching approach.

import pytest

def func(x):
    if x%2==0:
        return x+5
    else:
        return x-5

@pytest.mark.syed
def test_case_by_Mohit():
    assert func(3) == -2

@pytest.mark.syed
def test_case_by_Urmimala1():
    assert func(2) == 7

def test_case_by_Urmimala2():
    assert func(4) == 7

# substring test_method is present in both the test cases
# we pass substring to match by "-k" flag

#cmd: py.test -k test_case -v
# run all the test

# cmd: py.test -k test_case_by_U -v
# it will only test cases which contains the string test_case_by_U