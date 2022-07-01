from typing import List
from tester import Tester


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        nrow = len(matrix)
        ncol = len(matrix[0])
        length = 0
        for i in range(nrow):
            for j in range(ncol):
                matrix[i][j] = int(matrix[i][j])
                if i and j and matrix[i][j]:
                    matrix[i][j] = 1 + min(
                        matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i - 1][j]
                    )
                length = max(length, matrix[i][j])
        return length * length


t = Tester(Solution())
t.test(
    16,
    [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "1", "1", "0"],
        ["1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["0", "0", "1", "1", "1"],
    ],
)
t.test(
    4,
    [
        ["1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["0", "0", "0", "0", "0"],
        ["1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
    ],
)


t.test(
    4,
    [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ],
)

t.test(1, [[0, 1], [0, 0]])

t.report()
