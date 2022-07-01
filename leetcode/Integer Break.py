# https://leetcode.com/problems/integer-break/
from tester import Tester


class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1: 1}

        def dfs(num):
            if num in dp:
                return dp[num]

            dp[num] = num if num != n else 0
            for i in range(1, num):
                val = dfs(i) * dfs(num - i)
                dp[num] = max(dp[num], val)

            return dp[num]

        return dfs(n)


t = Tester(Solution())

t.test(1, 2)
t.test(2, 3)
t.test(4, 4)
t.test(36, 10)

t.report()
