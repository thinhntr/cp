# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        i = j = 0
        max_sum = prices[j] - prices[i]
        cur_sum = max_sum

        for k in range(1, n):
            ik_sum = prices[k] - prices[i]
            jk_sum = prices[k] - prices[j]

            if ik_sum > jk_sum:
                j = k
                cur_sum = ik_sum
            else:
                i, j = j, k
                cur_sum = jk_sum

            if cur_sum > max_sum:
                max_sum = cur_sum

        return max(0, max_sum)

    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0
        for price in prices:
            cur_profit = price - min_price
            if price < min_price:
                min_price = price
            elif profit < cur_profit:
                profit = cur_profit
        return profit


solution = Solution()


def check(inp, expected):
    output = solution.maxProfit(inp)
    assert output == expected


check([7, 1, 5, 3, 6, 4], 5)
check([7, 6, 4, 3, 1], 0)
check([4], 0)
