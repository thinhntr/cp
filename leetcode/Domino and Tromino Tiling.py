# https://leetcode.com/problems/domino-and-tromino-tiling/
from tester import Tester


class Solution:
    _dp = [[0] * 2 for _ in range(1001)]

    def numTilings(self, n: int, missing: int = 0) -> int:
        if n < 3:
            return n
        if Solution._dp[n][missing]:
            return Solution._dp[n][missing]
        total = 0
        if missing:
            total = self.numTilings(n - 1, 0) + self.numTilings(n - 1, 1)
        else:
            total = (
                self.numTilings(n - 1, 0)
                + self.numTilings(n - 2, 0)
                + self.numTilings(n - 2, 1) * 2
            )
        total %= 1_000_000_007
        Solution._dp[n][missing] = total
        return total


t = Tester(Solution())

t.test(1, 1)
t.test(2, 2)
t.test(5, 3)
t.test(11, 4)
t.test(24, 5)
t.test(312342182, 30)

t.report()
