# https://leetcode.com/problems/burst-balloons/
from typing import List
from tester import Tester


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0, 1)
        nums.append(1)
        n = len(nums)
        dp = [[-1] * n for _ in range(n)]

        def split(l, r):
            if dp[l][r] != -1:
                return dp[l][r]

            dp[l][r] = 0
            for m in range(l, r):
                tmp = split(l, m) + split(m + 1, r) + nums[l - 1] * nums[r] * nums[m]
                dp[l][r] = max(dp[l][r], tmp)
            return dp[l][r]

        return split(1, n - 1)


t = Tester(Solution())

t.test(5, [5])
t.test(10, [1, 5])
t.test(32, [3, 8])
t.test(167, [3, 1, 5, 8])

t.report()
