"""
Medium
You are given an unordered array consisting of consecutive integers
[1, 2, 3, ..., n] without any duplicates. You are allowed to swap any
two elements. Find the minimum number of swaps required to sort the
array in ascending order.

Can use numpy.argmin to find min but nupmy is not allowed for this 
problem on Hackerrank.
"""

import math
import numpy as np


def find_min(arr, lt, rt, target):
    half = math.floor((lt + rt) / 2)
    if arr[half] == target:
        return half
    if lt == rt:
        return -1
    m1 = find_min(arr, lt, half, target)
    if arr[m1] == target:
        return m1
    return find_min(arr, half + 1, rt, target)


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    min_swaps = 0
    for i in range(len(arr)):
        # check if arr[i] is in the correct order
        if arr[i] == (i + 1):
            continue
        # find the number that goes in arr[i]
        min_i = find_min(arr, i, len(arr) - 1, i + 1)
        if arr[min_i] == (i + 1):
            tmp = arr[i]
            arr[i] = arr[min_i]
            arr[min_i] = tmp
            min_swaps += 1
    return min_swaps
