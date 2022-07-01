# https://leetcode.com/problems/game-of-life/
from typing import List
from tester import Tester
import numpy as np

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board_copy = np.array(board)
        nrow, ncol = board_copy.shape
        for i in range(nrow):
            for j in range(ncol):
                start_row = max(0, i - 1)
                end_row = i + 2
                start_col = max(0, j - 1)
                end_col = j + 2
                neighbors = np.sum(board_copy[start_row:end_row, start_col:end_col]) - board[i][j]
                if neighbors == 3:
                    board[i][j] = 1
                elif neighbors < 2 or neighbors > 3:
                    board[i][j] = 0
        return board


t = Tester(Solution())

t.test(
    [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]],
    [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]],
)
t.test([[1, 1], [1, 1]], [[1, 1], [1, 0]])

t.report()
