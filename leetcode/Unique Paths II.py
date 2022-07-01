# https://leetcode.com/problems/unique-paths-ii/
from typing import List

from tester import Tester

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        nrow, ncol = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * ncol for _ in range(nrow)]
        dp[0][0] = 1
        for i in range(nrow):
            for j in range(ncol):
                if i:
                    dp[i][j] = dp[i - 1][j]
                if j:
                    dp[i][j] += dp[i][j - 1]
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
        return dp[-1][-1]

t = Tester(Solution())

t.test(0, [[1]])
t.test(1, [[0]])
t.test(0, [[0, 1], [1, 0]])
t.test(2, [[0,0,0],[0,1,0],[0,0,0]])
t.test(1, [[0,1],[0,0]])

t.report()