"""
Given a signed 32-bit integer x, return x with its digits reversed. If
reversing x causes the value to go outside the signed 32-bit integer range
[-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Constraints:
-231 <= x <= 231 - 1
"""


class Solution:
    def reverse(self, x: int) -> int:
        xs_arr = [c for c in str(x)]
        xs_arr.reverse()
        is_negative = False
        if x < 0:
            xs_arr = xs_arr[:-1]
            is_negative = True
        xs = ""
        for c in xs_arr:
            xs += c
        xr = int(xs)
        if is_negative:
            xr *= -1
        if (-(2**31)) <= xr and xr <= (2**31 - 1):
            return xr
        return 0
