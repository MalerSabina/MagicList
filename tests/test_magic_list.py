from contextlib import contextmanager

from magic_list import MagicList
import pytest
from pytest import raises


def test_zero_index_boundary():
    # Valid boundary access check, expecting append to list
    a = MagicList()
    a[0] = 5
    assert a[0] == 5

def test_minus_one_index_boundary():
    # Valid boundary access check, expecting append to list
    a = MagicList()
    a[-1] = 5

def test_skip_valid_boundary():
    # Valid boundary access check, expecting append it to list
    a = MagicList()
    for i in range(5):
        assert a == list(range(i))
        a[i] = i

def test_skip_valid_negative_boundary():
    # Valid boundary access check, expecting append it to list
    a = MagicList()
    for i in range(5):
        assert a == list(range(i))
        a[-1] = i

# Creates multiple variants of a test with different values as arguments
# The first argument parameter names.
# The second argument is a sequence of numbers that represent the parameter value(s).
@pytest.mark.parametrize("index", range(2, 5))
def test_upper_index_boundary(index):
    # Invalid boundary access check, expecting append to list
    a = MagicList()
    with raises(IndexError):
        a[index] = 5

@pytest.mark.parametrize("index", range(2, 5))
def test_negative_index_boundary(index: int):
    # Invalid boundary access check, expecting append to list
    a = MagicList()
    with raises(IndexError):
        a[-index] = 5

if __name__ == '__main__':
    pytest.main()