"""Starting with a 1-indexed array of zeros and a list of operations,for each
operation add a value to each the array element between two given indices,
inclusive. Once all operations have been performed, return the maximum value
in the array.

Example
n = 10
queries = [[1,5,3],[4,8,7],[6,9,1]]

Queries are interpreted as follows:

a b k
1 5 3
4 8 7
6 9 1

Add the values of k between the indices a and b inclusive.

Numpy is not available in Hackerank for this problem.

Doesn't pass all tests on HackerRank. Mainly tests with high values of n and q.
Downloaded test answer = 2490686975
"""

import numpy as np


def array_manipulation(n, queries):
    array = [0] * n
    for q in queries:
        a, b, k = q[0], q[1], q[2]
        array = array[: a - 1] + [v + k for v in array[a - 1 : b]] + array[b:]
    return max(array)


def array_manipulation_np(n, queries):
    # array size n filled with 0's of type int
    arr_np = np.zeros(n, int)
    for query in queries:
        a, b, k = query[0], query[1], query[2]
        tmp = arr_np[a:b]
        tmp[:] += k
    return arr_np.max()
