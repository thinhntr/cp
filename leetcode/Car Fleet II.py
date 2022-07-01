# https://leetcode.com/problems/car-fleet-ii/
from typing import List

from tester import Tester


class Solution:
    def getCollisionTimes(self, A: List[List[int]]) -> List[float]:
        n = len(A)
        stack = []
        res = [-1.0] * n
        get_time = lambda i, j: (A[j][0] - A[i][0]) / (A[i][1] - A[j][1])
        for i in range(n - 1, -1, -1):
            while stack and (
                A[i][1] <= A[stack[-1]][1]
                or get_time(i, stack[-1]) >= res[stack[-1]] > 0
            ):
                stack.pop()
            if stack:
                res[i] = get_time(i, stack[-1])
            stack.append(i)
        return res


t = Tester(Solution())

t.test([2.00000, 1.00000, 1.50000, -1.00000], [[3, 4], [5, 4], [6, 3], [9, 1]])
t.test([1.00000, -1.00000, 3.00000, -1.00000], [[1, 2], [2, 1], [4, 3], [7, 2]])

t.report()
