# https://leetcode.com/problems/maximal-rectangle/
from collections import deque
from typing import List
from tester import Tester


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        nrow = len(matrix)
        ncol = len(matrix[0])

        # Calculate prefix sum from top to bottom
        for i in range(nrow):
            for j in range(ncol):
                matrix[i][j] = 1 if matrix[i][j] == "1" else 0
                if 0 < i and matrix[i][j]:
                    matrix[i][j] += matrix[i - 1][j]

        # Nearest smaller item's index from left
        nsl = [[-1] * ncol for _ in range(nrow)]
        for i in range(nrow):
            stack = deque()
            for j in reversed(range(ncol)):
                while stack and matrix[i][j] < matrix[i][stack[-1]]:
                    nsl[i][stack.pop()] = j
                stack.append(j)

        # Nearest smaller item's index from right
        nsr = [[ncol] * ncol for _ in range(nrow)]
        for i in range(nrow):
            stack = deque()
            for j in range(ncol):
                while stack and matrix[i][j] < matrix[i][stack[-1]]:
                    nsr[i][stack.pop()] = j
                stack.append(j)

        # Find max area
        area = 0
        for i in range(nrow):
            for j in range(ncol):
                area = max(area, matrix[i][j] * (nsr[i][j] - nsl[i][j] - 1))
        return area


t = Tester(Solution())

t.test(
    6,
    [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ],
)
t.test(1, [["1", "0"]])
t.test(0, [["0"]])
t.test(1, [["1"]])

t.report()
