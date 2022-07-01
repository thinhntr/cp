# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        min_buy = float('-inf')
        profit = 0
        for price in prices:
            min_buy = max(min_buy, profit - price - fee)
            profit = max(profit, price + min_buy)
        return profit

solution = Solution()


def check(input, expected):
    output = solution.maxProfit(*input)
    assert output == expected


check([[1, 3, 2, 8, 4, 9], 2], 8)
check([[1, 3, 7, 5, 10, 3], 3], 6)
check([[5, 9, 10, 1, 2, 9], 3], 7)
