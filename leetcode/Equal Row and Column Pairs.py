# https://leetcode.com/problems/equal-row-and-column-pairs/
from collections import Counter
from typing import List

from tester import Tester


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        arr2string = lambda row: " ".join(map(str, row))
        counter = Counter(arr2string(row) for row in grid)
        total = 0
        for j in range(ncol):
            s = arr2string(grid[i][j] for i in range(nrow))
            total += counter[s]
        return total


t = Tester(Solution())

t.test(1, [[3, 2, 1], [1, 7, 6], [2, 7, 7]])
t.test(3, [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]])

t.report()
