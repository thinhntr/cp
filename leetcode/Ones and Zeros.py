# https://leetcode.com/problems/ones-and-zeroes/
from typing import List

import numpy as np

from tester import Tester


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = np.zeros((m + 1, n + 1), dtype=int)
        for s in strs:
            zeros = s.count("0")
            ones = len(s) - zeros
            if m < zeros or n < ones:
                continue
            dp[zeros : m + 1, ones : n + 1] = np.maximum(
                dp[zeros : m + 1, ones : n + 1], dp[: m + 1 - zeros, : n + 1 - ones] + 1
            )

        return dp[m][n]


t = Tester(Solution())

t.test(0, ["000", "00"], 1, 10)
t.test(4, ["10", "0001", "111001", "1", "0"], 5, 3)
t.test(2, ["10", "0", "1"], 1, 1)

t.test(3, ["10", "0001", "111001", "1", "0"], 3, 2)

t.report()
