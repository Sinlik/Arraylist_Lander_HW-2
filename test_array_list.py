from array_list import ArrayList
import pytest

@pytest.fixture
def lst():
    l = ArrayList()
    l.add('a')
    l.add('b')
    return l

def test_add(lst):
    lst.add('c')
    assert lst.get(2) == 'c'

def test_remove(lst):
    assert lst.remove(1) == 'b'

def test_get(lst):
    assert lst.get(1) == 'b'

def test_set(lst):
    lst.set(1, 's')
    assert lst.get(1) == 's'

def test_getIndex(lst):
    assert lst.getIndex('d') == -1
    assert lst.getIndex('a') == 0

def test_size(lst):
    assert lst.size() == 2