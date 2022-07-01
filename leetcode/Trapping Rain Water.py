# https://leetcode.com/problems/trapping-rain-water/
from operator import itemgetter
from typing import List

from tester import Tester


class Solution:
    def trap(self, height: List[int]) -> int:
        max_idx, _ = max(enumerate(height), key=itemgetter(1))
        res, ph = 0, height[0]

        for ch in height[1:max_idx]:
            if ph > ch:
                res += ph - ch
            else:
                ph = ch

        ph = height[len(height) - 1]
        for ch in height[len(height) - 1 : max_idx : -1]:
            if ph > ch:
                res += ph - ch
            else:
                ph = ch
        return res


t = Tester(Solution())

t.test(6, [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
t.test(9, [4, 2, 0, 3, 2, 5])
t.test(23, [3, 0, 0, 4, 5, 0, 0, 3, 0, 5])

t.report()
