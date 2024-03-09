import pytest

from new_year_chaos import minimum_bribes


@pytest.mark.parametrize(("q", "expected"), [([1, 2, 5, 3, 7, 8, 6, 4], "7")])
def test_minimum_bribes(q, expected):
    assert expected == minimum_bribes(q)
