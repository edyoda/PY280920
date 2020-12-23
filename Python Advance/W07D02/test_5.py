## Fixtures : They are used to have something pre run before the test.

# very similar to __init__.py file in a package

import pytest

# @pytest.fixture
def pre_data():
    # requirements to run a code.
    data = {"python":3,"django":2,"numpy":1}
    return data

def test_case_1(pre_data):
    python = 3
    assert pre_data["python"] == python

def test_case_2(pre_data):
    django = 1
    assert pre_data["django"] == django