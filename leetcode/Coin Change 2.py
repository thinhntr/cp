# https://leetcode.com/problems/coin-change-2
from typing import List

from tester import Tester


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """DP"""
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n)]

        for i in range(n):
            for m in range(amount + 1):
                if not m:
                    dp[i][m] = 1
                    continue
                remain = m - coins[i]
                if remain >= 0:
                    dp[i][m] += dp[i][remain]
                if i:
                    dp[i][m] += dp[i - 1][m]
        return dp[-1][-1]


t = Tester(Solution())

t.test(4, 5, [1, 2, 5])
t.test(0, 3, [2])
t.test(1, 10, [10])
t.test(1, 100, [1, 101, 102, 103])

t.report()
