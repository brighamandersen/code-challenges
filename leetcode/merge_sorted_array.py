import math
from typing import List

# https://leetcode.com/problems/merge-sorted-array/


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        index1 = m - 1
        index2 = n - 1

        for result_index in reversed(range(m + n)):
            if index1 >= 0:
                n1 = nums1[index1]
            else:
                n1 = -math.inf

            if index2 >= 0:
                n2 = nums2[index2]
            else:
                n2 = -math.inf

            if n2 > n1:
                nums1[result_index] = n2
                index2 -= 1
            else:
                nums1[result_index] = n1
                index1 -= 1
