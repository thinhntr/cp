# https://leetcode.com/problems/minimum-path-sum/
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        nr, nc = len(grid), len(grid[0])

        for c in reversed(range(nc - 1)):
            grid[-1][c] += grid[-1][c + 1]

        for r in reversed(range(nr - 1)):
            grid[r][-1] += grid[r + 1][-1]

        for r in reversed(range(nr - 1)):
            for c in reversed(range(nc - 1)):
                grid[r][c] += min(grid[r + 1][c], grid[r][c + 1])

        return grid[0][0]


solution = Solution()


def check(input, expected):
    output = solution.minPathSum(input)
    assert output == expected


check([[1, 3, 1],
       [1, 5, 1],
       [4, 2, 1]], 7)

check([[1, 2, 3],
       [4, 5, 6]], 12)
