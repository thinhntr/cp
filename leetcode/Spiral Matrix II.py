# https://leetcode.com/problems/spiral-matrix-ii/
from typing import List
from tester import Tester


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        r1 = c1 = 0
        r2 = c2 = n - 1
        val = 1
        while r1 <= r2 and c1 <= c2:
            for i in range(c1, c2 + 1):
                res[r1][i] = val
                val += 1
            for i in range(r1 + 1, r2 + 1):
                res[i][c2] = val
                val += 1
            for i in range(c2 - 1, c1, -1):
                res[r2][i] = val
                val += 1
            for i in range(r2, r1, -1):
                res[i][c1] = val
                val += 1
            r1 += 1
            c1 += 1
            r2 -= 1
            c2 -= 1
        return res


t = Tester(Solution())

t.test([[]])
t.test([[1, 2, 3], [8, 9, 4], [7, 6, 5]], 3)
t.test([[1]], 1)

t.report()
