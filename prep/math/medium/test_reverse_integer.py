import pytest

from reverse_integer import Solution


@pytest.mark.parametrize(
    ("num", "expected"),
    [
        (123, 321),
        (-123, -321),
        ((-(2**31) - 1), 0),
        (-8463847412, -(2**31)),
        (2**31, 0),
        (7463847412, (2**31) - 1),
    ],
)
def test_reverse_integer(num, expected):
    assert expected == Solution().reverse(num)
