import os

import doctest
import pytest

import right
import solution
import wrong1
import wrong2
import wrong3


@pytest.fixture(name='custom_sort')
def _custom_sort():
    name = os.environ['FUNCTION_VERSION']
    return {
        "user_implementation": solution,
        "right": right,
        "wrong1": wrong1,
        "wrong2": wrong2,
        "wrong3": wrong3,
    }[name].custom_sort


# BEGIN (write your solution here)
import pytest


@pytest.fixture
def coll():
    return [1, 5, 2, 12]


@pytest.fixture
def empty():
    return []


def test_custom_sort(custom_sort, coll):
    assert custom_sort(coll) == [1, 2, 5, 12]
    assert custom_sort(coll, True) == [12, 5, 2, 1]


def test_custom_sort_empty(custom_sort, empty):
    assert custom_sort(empty) == []
    assert custom_sort(empty, True) == []

# END
def test_doctest(custom_sort):
    module = custom_sort.__module__
    module = __import__(module)

    failed, attempted = doctest.testmod(module)
    assert failed == 0
    assert attempted == 3









