# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
from functools import cache
from typing import List

from tester import Tester


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = {}  # {(r,c)->max}

        def dfs(i, j, prev):
            if not (0 <= i < m and 0 <= j < n) or prev >= matrix[i][j]:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            res = 1
            res = max(res, 1 + dfs(i + 1, j, matrix[i][j]))
            res = max(res, 1 + dfs(i - 1, j, matrix[i][j]))
            res = max(res, 1 + dfs(i, j + 1, matrix[i][j]))
            res = max(res, 1 + dfs(i, j - 1, matrix[i][j]))
            dp[(i, j)] = res
            return res

        for i in range(m):
            for j in range(n):
                dfs(i, j, -1)
        return max(dp.values())


t = Tester(Solution())

t.test(6, [[7, 8, 9], [9, 7, 6], [7, 2, 3]])
t.test(4, [[9, 9, 4], [6, 6, 8], [2, 1, 1]])
t.test(4, [[3, 4, 5], [3, 2, 6], [2, 2, 1]])
t.test(1, [[1]])

t.report()
