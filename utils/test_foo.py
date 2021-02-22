# how to write tests and assert things

import pytest
from foo_lib import foo


@pytest.fixture
def setup_something():
    """a function to create fixed values. Can be seen as a setup function

    Returns:
        int: a fixed value
    """
    value = 2
    return value


def test_foo():
    assert foo(1) == 2


def test_with_type_error_foo():
    with pytest.raises(TypeError):
        foo('bah')


def test_with_fixture(setup_something):
    assert setup_something == 2
