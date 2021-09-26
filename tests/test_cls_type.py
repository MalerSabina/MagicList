from magic_list import MagicList
from person import Person
import pytest
from contextlib import contextmanager


def test_init_assigned_types():
    # Magic list with valid boundary access cls_type argument, create new instance of class.
    a = MagicList(cls_type=Person)
    a[0].age = 5
    assert a[0] == Person(age=5)

def test_enforce_indexes_continuity():
    # Magic list with invalid boundary access of cls_type argument
    a = MagicList(cls_type=Person)
    with pytest.raises(IndexError):
        a[1].age = 5

if __name__ == '__main__':
    pytest.main()
