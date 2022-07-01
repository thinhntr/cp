# https://leetcode.com/problems/shift-2d-grid/
from typing import List
from tester import Tester
from numpy import array, ravel, flip


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        grid = array(grid)
        n = grid.size
        k %= n
        flatten = ravel(grid)
        flatten[: n - k] = flip(flatten[: n - k])
        flatten[n - k :] = flip(flatten[n - k :])
        return flip(grid).tolist()


t = Tester(Solution())

t.test([[9, 1, 2], [3, 4, 5], [6, 7, 8]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1)
t.test([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9)
t.test([[6], [5], [1], [2], [3], [4], [7]], [[1], [2], [3], [4], [7], [6], [5]], 23)

t.report()
