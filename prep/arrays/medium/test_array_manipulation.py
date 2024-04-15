import pytest
from prep.arrays.medium.array_manipulation import array_manipulation


@pytest.mark.parametrize(
    ("n", "queries", "expected"),
    [
        (10, [[1, 5, 3], [4, 8, 7], [6, 9, 1]], 10),
        (5, [[1, 2, 100], [2, 5, 100], [3, 4, 100]], 200),
        (10, [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]], 31),
        (5, [[1, 5, 1], [2, 5, 2], [3, 5, 3], [4, 5, 4], [5, 5, 5]], 15),
        (5, [[1, 1, 5], [1, 2, 4], [1, 3, 3], [1, 4, 2], [1, 5, 1]], 15),
    ],
)
def test_array_manipulation(n, queries, expected):
    assert expected == array_manipulation(n, queries)
