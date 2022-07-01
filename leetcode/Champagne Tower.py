# https://leetcode.com/problems/champagne-tower/
from typing import List
from tester import Tester


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        res = [poured] + [0] * query_row
        for row in range(1, query_row + 1):
            for i in range(row, -1, -1):
                res[i] = max(res[i] - 1, 0) / 2.0 + max(res[i - 1] - 1, 0) / 2.0
        return min(res[query_glass], 1)


t = Tester(Solution())

t.test(1, 5, 1, 0)
t.test(0.25, 4, 2, 0)
t.test(1, 3, 1, 1)
t.test(0.5, 4, 2, 1)
t.test(0, 1, 1, 1)
t.test(0.5, 2, 1, 1)
t.test(1, 100000009, 33, 17)

t.report()

# 2 0 0
# 2 1 1
