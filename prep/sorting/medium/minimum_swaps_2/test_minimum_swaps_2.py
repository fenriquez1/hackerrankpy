import pytest
from prep.sorting.medium.minimum_swaps_2.minimum_swaps_2 import minimumSwaps

""" 14/14 tests pass on hackerrank with solution.
"""


@pytest.mark.parametrize(
    ("arr", "expected"), [([7, 1, 3, 2, 4, 5, 6], 5), ([4, 3, 1, 2], 3)]
)
def test_minimum_swaps(arr, expected):
    # WHEN
    actual = minimumSwaps(arr)

    # THEN
    assert actual == expected
