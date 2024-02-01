"""
# Easy
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 
respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored 
inside the array nums1. To accommodate this, nums1 has a length of m + n, where the 
first m elements denote the elements that should be merged, and the last n elements 
are set to 0 and should be ignored. nums2 has a length of n.
"""

from typing import List
from collections import deque


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1_it = 0
        nums2_it = 0
        tmp = 0
        dq = deque()
        while nums1_it < len(nums1):
            qnum = 0
            if len(dq) > 0:
                qnum = dq.popleft()
            n1 = nums1[nums1_it]
            n2 = nums2[nums2_it] if nums2_it < len(nums2) else 0
            num = self.compare(n1, n2, qnum)
            if num == nums1[nums1_it]:
                nums1_it += 1
                if qnum > 0:
                    dq.appendleft(qnum)
            elif nums2_it < len(nums2) and num == nums2[nums2_it]:
                dq.append(nums1[nums1_it])
                nums1[nums1_it] = nums2[nums2_it]
                nums1_it += 1
                nums2_it += 1
                if qnum > 0:
                    dq.appendleft(qnum)
            elif num == qnum:
                dq.append(nums1[nums1_it])
                nums1[nums1_it] = qnum
                nums1_it += 1

    def compare(self, n1: int, n2: int, n3: int) -> int:
        if n1 > 0 and n2 > 0 and n3 > 0:
            return min(n1, min(n2, n3))
        if n1 == 0:
            if n2 == 0:
                return n3
            if n3 == 0:
                return n2
            return min(n2, n3)
        if n2 == 0:
            if n3 == 0:
                return n1
            return min(n1, n3)
        if n3 == 0:
            return min(n1, n2)
