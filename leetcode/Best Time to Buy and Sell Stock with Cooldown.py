# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
from typing import List


class Solution:
    def maxProfit(self, prices):
        b, c, s = float('-inf'), 0, 0
        for p in prices:
            b = max(b, c - p)
            c = max(c, s)
            s = b + p
        return max(c, s)


solution = Solution()


def check(input, expected):
    output = solution.maxProfit(input)
    assert output == expected


check([1, 2, 3, 0, 2], 3)
check([1], 0)
check([8, 9, 10, 1, 2, 9], 9)
check([8, 9, 10, 1, 3, 9], 9)
check([2, 4, 6, 1, 3, 5, 4, 8, 9], 10)
