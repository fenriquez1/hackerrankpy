import pytest
from prep.sorting.medium.minimum_swaps_2.minimum_swaps_2 import minimumSwaps

""" 9/14 tests pass on hackerrank with solution but I get error:
Time limit exceeded
Your code did not execute within the time limits. Please optimize
your code. For more information on execution time limits, refer 
to the environment page
"""


@pytest.mark.parametrize(("arr", "expected"), [([7, 1, 3, 2, 4, 5, 6], 5)])
def test_minimum_swaps(arr, expected):
    # WHEN
    actual = minimumSwaps(arr)

    # THEN
    assert actual == expected
