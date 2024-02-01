from prep.sorting.easy.merge_sorted_array.merge_sorted_array import Solution

import pytest


@pytest.mark.parametrize(
    ("nums1", "m", "nums2", "expected"),
    [
        (
            [1, 3, 5, 7, 9, 0, 0, 0, 0, 0],
            5,
            [2, 4, 6, 8, 10],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        ),
        (
            [2, 4, 6, 8, 10, 0, 0, 0, 0, 0],
            5,
            [1, 3, 5, 7, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        ),
        (
            [2, 4, 6, 8, 10, 0, 0, 0, 0, 0],
            5,
            [12, 13, 15, 17, 19],
            [2, 4, 6, 8, 10, 12, 13, 15, 17, 19],
        ),
        (
            [12, 13, 15, 17, 19, 0, 0, 0, 0, 0],
            5,
            [2, 4, 6, 8, 10],
            [2, 4, 6, 8, 10, 12, 13, 15, 17, 19],
        ),
    ],
)
def test_merge(nums1, m, nums2, expected):
    # WHEN
    Solution().merge(nums1=nums1, m=m, nums2=nums2, n=len(nums2))

    # THEN
    assert m + len(nums2) == len(nums1)
    assert nums1 == expected


@pytest.mark.parametrize(
    ("n1", "n2", "n3", "expected"),
    [
        (1, 2, 3, 1),
        (1, 3, 2, 1),
        (2, 1, 3, 1),
        (2, 3, 1, 1),
        (3, 2, 1, 1),
        (0, 1, 2, 1),
        (1, 0, 2, 1),
        (1, 2, 0, 1),
        (0, 0, 1, 1),
        (0, 1, 0, 1),
        (1, 0, 0, 1),
    ],
)
def test_compare(n1, n2, n3, expected):
    # THEN
    assert Solution().compare(n1, n2, n3) == expected
