# https://leetcode.com/problems/range-sum-query-2d-immutable/
from typing import List

from tester import ObjectTester

class Solution:
    def __init__(self, a=None):
        self.a = a if a else 5
        
    def something_for_your_mind(self):
        if self.a == 2:
            return 5


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                matrix[r][c] = matrix[r][c]
                if r:
                    matrix[r][c] += matrix[r - 1][c]
                if c:
                    matrix[r][c] += matrix[r][c - 1]
                if r and c:
                    matrix[r][c] -= matrix[r - 1][c - 1]
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        matrix = self.matrix
        result = matrix[row2][col2]
        if col1:
            result -= matrix[row2][col1 - 1]
        if row1:
            result -= matrix[row1 - 1][col2]
        if row1 and col1:
            result += matrix[row1 - 1][col1 - 1]
        return result


if __name__ == "__main__":
    o = ObjectTester(__file__)
    o.test(
        [None, 8, 11, 12],
        ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"],
        [
            [
                [
                    [3, 0, 1, 4, 2],
                    [5, 6, 3, 2, 1],
                    [1, 2, 0, 1, 5],
                    [4, 1, 0, 1, 7],
                    [1, 0, 3, 0, 5],
                ]
            ],
            [2, 1, 4, 3],
            [1, 1, 2, 2],
            [1, 2, 2, 4],
        ],
    )
    o.report()
