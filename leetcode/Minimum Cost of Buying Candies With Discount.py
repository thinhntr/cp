# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/
from typing import List
from tester import Tester


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n = len(cost)
        cost.sort()

        total = 0
        for i in range(n - 1, -1, -3):
            total += cost[i] + (cost[i - 1] if i > 0 else 0)
        return total


t = Tester(Solution())

t.test(2, [2])
t.test(3, [1, 2])
t.test(5, [1, 2, 3])
t.test(8, [1, 2, 3, 4])
t.test(23, [6, 5, 7, 9, 2, 2])

t.report()
