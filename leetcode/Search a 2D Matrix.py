# https://leetcode.com/problems/search-a-2d-matrix/
from typing import List
from tester import Tester


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrow, ncol = len(matrix), len(matrix[0])
        l, r = 0, nrow * ncol - 1
        while l <= r:
            m = (l + r) // 2
            mid = matrix[m // ncol][m % ncol]
            if mid == target:
                return True
            elif mid < target:
                l = m + 1
            else:
                r = m - 1
        return False


t = Tester(Solution())

t.test(True, [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
t.test(False, [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)

t.report()
