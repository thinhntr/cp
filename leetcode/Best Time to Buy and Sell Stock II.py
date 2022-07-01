# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices.append(-1)
        profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]:
                if prices[i - 1] > min_price:
                    profit += prices[i - 1] - min_price
                min_price = prices[i]
        return profit


solution = Solution()


def check(input, expected):
    output = solution.maxProfit(input)
    assert output == expected


check([7, 1, 5, 3, 6, 4], 7)
check([1, 2, 3, 4, 5], 4)
check([7, 6, 4, 3, 1], 0)
check([6, 9], 3)
check([7, 6], 0)
check([8, 6], 0)
check([5, 1], 0)
check([0], 0)
check([1], 0)
check([2], 0)
check([7], 0)
