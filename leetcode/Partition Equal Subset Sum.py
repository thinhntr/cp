# https://leetcode.com/problems/partition-equal-subset-sum/
from typing import List

from tester import Tester


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """Top-down DP"""
        total = sum(nums)
        if total % 2:
            return False

        target = total // 2
        dp = {}  # {(target, idx): True,...}

        def helper(target, idx):
            if target < 0 or len(nums) <= idx:
                return False
            elif target == 0:
                return True
            elif (target, idx) in dp:
                return dp[(target, idx)]
            res = helper(target - nums[idx], idx + 1) or helper(target, idx + 1)
            dp[(target, idx)] = res
            return res

        return helper(target, 0)

    def canPartition(self, nums: List[int]) -> bool:
        """Bottom-up DP"""
        total = sum(nums)
        if total % 2:
            return False

        n = len(nums)
        target = total // 2
        dp = [[False] * (target + 1) for _ in range(n)]

        for i in range(n):
            for t in range(target + 1):
                remain = t - nums[i]
                if remain == 0 or t == 0:
                    dp[i][t] = True
                else:
                    dp[i][t] = dp[i - 1][t] or (remain > 0 and dp[i - 1][remain])
                if t == target and dp[i][t]:
                    return True

        return dp[-1][-1]


t = Tester(Solution())

t.test(True, [1, 5, 10, 6])
t.test(False, [1, 2, 5])
t.test(True, [1, 5, 11, 5])
t.test(False, [1, 2, 3, 5])

t.report()
