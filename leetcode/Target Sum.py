# https://leetcode.com/problems/target-sum/
from functools import cache
from typing import List

from tester import Tester


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @cache
        def helper(i, total):
            if i == n:
                return 1 if total == target else 0
            return helper(i + 1, total + nums[i]) + helper(i + 1, total - nums[i])

        return helper(0, 0)


t = Tester(Solution())

t.test(1, [1, 1], 2)
t.test(5, [1, 1, 1, 1, 1], 3)
t.test(1, [1], 1)

t.report()
