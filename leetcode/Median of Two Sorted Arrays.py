# https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import List
from tester import Tester


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        total = len(n1) + len(n2)
        half = total // 2
        l, r = 0, len(n1) - 1
        
        while True:
            m1 = (l + r) // 2
            m2 = half - m1 - 2

            mid1 = n1[m1] if 0 <= m1 else float("-inf")
            mid11 = n1[m1 + 1] if m1 + 1 < len(n1) else float("inf")
            mid2 = n2[m2] if 0 <= m2 else float("-inf")
            mid21 = n2[m2 + 1] if m2 + 1 < len(n2) else float("inf")

            if mid1 > mid21:
                r = m1 - 1
            elif mid2 > mid11:
                l = m1 + 1
            else:
                return (
                    min(mid11, mid21)
                    if total % 2
                    else (max(mid1, mid2) + min(mid11, mid21)) / 2
                )


t = Tester(Solution())

t.test(2.5, [], [2, 3])
t.test(1, [], [1])
t.test(3.5, [1], [2, 3, 4, 5, 6])
t.test(6.5, [5, 7], [6, 8])
t.test(6.5, [6, 7], [5, 8])
t.test(6.5, [5, 5, 5], [8, 8, 8])
t.test(5, [5, 5, 5], [5, 8, 8])
t.test(8, [5, 5, 8], [8, 8, 8])
t.test(7, [5, 5, 5], [7, 8, 8, 8])
t.test(8, [5, 5, 5], [8, 8, 8, 8])
t.test(7, [5, 5, 5, 7], [8, 8, 8])
t.test(8, [5, 5, 5, 8], [8, 8, 8])
t.test(2.5, [1, 2], [3, 4])
t.test(2, [1, 3], [2])

t.report()
