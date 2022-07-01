# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
from typing import List


class Solution:
    def countNegatives(self, grid):
        nrows, ncols = len(grid), len(grid[0])
        count = 0
        c = ncols - 1
        r = 0
        while c >-1:
            if grid[r][c] < 0:
                count += nrows - r
                c -= 1
            elif r < nrows - 1: 
                r += 1
            else:
                break
        return count


solution = Solution()


def check(input, expected):
    output = solution.countNegatives(input)
    assert output == expected


check([[ 4,   3,    2, -1],
       [ 3,   2,    1, -1],
       [ 1,   1,   -1, -2],
       [-1,  -1,   -2, -3]], 8)

check([[3, 2], 
       [1, 0]], 0)

check([[ 1, -1],
       [-1, -1]], 3)

check([[-1]], 1)
