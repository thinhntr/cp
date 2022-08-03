# https://leetcode.com/problems/max-area-of-island/
from typing import List, Set, Tuple

from tester import Tester


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """Recursive DFS"""
        m, n = len(grid), len(grid[0])
        visited: Set[Tuple[int, int]] = set()

        def dfs(i, j):
            if (
                (i, j) in visited
                or i < 0
                or i >= m
                or j < 0
                or j >= n
                or not grid[i][j]
            ):
                return 0
            visited.add((i, j))
            area = 1
            area += dfs(i + 1, j)
            area += dfs(i - 1, j)
            area += dfs(i, j + 1)
            area += dfs(i, j - 1)
            return area

        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))
        return result


t = Tester(Solution())

t.test(0, [[0, 0, 0, 0, 0, 0, 0, 0]])

t.test(4, [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]])

t.test(
    6,
    [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ],
)

t.report()
