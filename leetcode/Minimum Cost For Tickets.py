# https://leetcode.com/problems/minimum-cost-for-tickets/
from typing import List
from tester import Tester


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        idx7 = idx30 = 0
        days.insert(0, 0)
        n = len(days)
        dp = [0] * n
        for i, day in enumerate(days[1:], 1):
            # Find the cost of 7 days before
            last7day = day - 7
            while 0 <= last7day and days[idx7 + 1] <= last7day:
                idx7 += 1

            # Find the cost of 30 days before
            last30day = day - 30
            while 0 <= last30day and days[idx30 + 1] <= last30day:
                idx30 += 1

            # 3 options to buy ticket
            cost1 = costs[0] + dp[i - 1]
            cost2 = costs[1] + dp[idx7]
            cost3 = costs[2] + dp[idx30]
            dp[i] = min(cost1, cost2, cost3)
        return dp[-1]


t = Tester(Solution())

t.test(11, [1, 4, 6, 7, 8, 20], [2, 7, 15])
t.test(17, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15])
t.test(9, [1, 4, 6, 8, 10], [2, 7, 15])

t.report()
