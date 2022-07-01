# https://leetcode.com/problems/minimum-falling-path-sum/
from typing import List
from tester import Tester


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        nrow = len(matrix)
        ncol = len(matrix[0])
        for i in reversed(range(nrow - 1)):
            for j in range(ncol):
                l = j - 1 if j else 0
                r = j + 2 if j + 1 < ncol else ncol
                matrix[i][j] += min(matrix[i+1][l:r])
        return min(matrix[0])


t = Tester(Solution())

t.test(
    -36,
    [[100, -42, -46, -41], 
     [ 31,  97,  10, -10], 
     [-58, -51,  82,  89], 
     [ 51,  81,  69, -51]],
)
t.test(-59, [[-19, 57], [-40, -5]])
t.test(13, [[2, 1, 3], [6, 5, 4], [7, 8, 9]])
t.report()
