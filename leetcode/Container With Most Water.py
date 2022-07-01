# https://leetcode.com/problems/container-with-most-water/
from typing import List
from tester import Tester


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            max_area = max(max_area, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


t = Tester(Solution())


t.test(49, [1, 8, 6, 2, 5, 4, 8, 3, 7])
t.test(1, [1, 1])
t.test(16, [4, 3, 2, 1, 4])
t.test(2, [1, 2, 1])

t.report()
