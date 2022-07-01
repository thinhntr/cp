# https://leetcode.com/problems/path-with-maximum-gold/
from typing import List

from tester import Tester


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if not (0 <= i < m) or not (0 <= j < n) or not grid[i][j]:
                return 0
            tmp = grid[i][j]
            grid[i][j] = 0
            up = dfs(i - 1, j)
            down = dfs(i + 1, j)
            left = dfs(i, j - 1)
            right = dfs(i, j + 1)
            grid[i][j] = tmp
            return tmp + max(up, down, left, right)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    res = max(res, dfs(i, j))
        return res


t = Tester(Solution())

t.test(24, [[0, 6, 0], [5, 8, 7], [0, 9, 0]])

t.test(28, [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]])

t.report()
