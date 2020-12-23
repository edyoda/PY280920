# how to transfer many test cases.

import pytest

check_list = [("3+5",8),("4*8",32),("5*4",20)]

@pytest.mark.parametrize("test_input,expected",check_list)
def test_eval(test_input,expected):
    assert eval(test_input) == expected

#eval evaluates the string as an Python expression.