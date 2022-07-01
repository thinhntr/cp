# https://leetcode.com/problems/set-matrix-zeroes/

from typing import List
from icecream import ic

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        nrow = len(matrix)
        ncol = len(matrix[0])

        row0 = False
        for i in range(ncol):
            if not matrix[0][i]:
                row0 = True
                break

        col0 = False
        for i in range(nrow):
            if not matrix[i][0]:
                col0 = True

            for j in range(ncol):
                if not matrix[i][j]:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in reversed(range(1, nrow)):
            for j in reversed(range(1, ncol)):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
            if col0:
                matrix[i][0] = 0

        if row0:
            for i in range(ncol):
                matrix[0][i] = 0


ic(Solution().setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
ic(Solution().setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
ic(Solution().setZeroes([[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]))
