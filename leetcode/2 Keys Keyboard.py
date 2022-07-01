# https://leetcode.com/problems/2-keys-keyboard/
from typing import List
from tester import Tester


class Solution:
    _dp = [-1] * 1001
    _dp[0] = 0
    _dp[1] = 0

    def minSteps(self, n: int) -> int:
        if Solution._dp[n] != -1:
            return Solution._dp[n]
        for i in range(n // 2, 0, -1):
            if not n % i:
                break
        Solution._dp[n] = n // i + self.minSteps(i)
        return Solution._dp[n]


t = Tester(Solution())

t.test(0, 1)
t.test(2, 2)
t.test(3, 3)
t.test(4, 4)
t.test(5, 5)
t.test(5, 6)
t.test(7, 7)
t.test(6, 8)
t.test(6, 9)
t.test(7, 10)
t.test(11, 11)
t.test(7, 12)

t.report()
