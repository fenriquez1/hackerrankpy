"""
Medium
You are given an unordered array consisting of consecutive integers
[1, 2, 3, ..., n] without any duplicates. You are allowed to swap any
two elements. Find the minimum number of swaps required to sort the
array in ascending order.

Can use numpy.argmin to find min but nupmy is not allowed for this 
problem on Hackerrank.

Using enumerate to create a dict {number: pos_in_array} allows fast
lookup and passes all tests.
"""


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    min_swaps = 0
    lookup = {key: val for val, key in enumerate(arr, start=1)}
    for i in range(len(arr)):
        # check if arr[i] is in the correct order
        if arr[i] == (i + 1):
            continue
        # find the number that goes in arr[i] and swap
        min_i = lookup[i + 1]
        tmp = arr[i]
        lookup[tmp] = min_i
        arr[i] = arr[min_i - 1]
        arr[min_i - 1] = tmp
        min_swaps += 1
    return min_swaps
