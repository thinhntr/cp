# https://leetcode.com/problems/sudoku-solver/
import string
from typing import List
from tester import Tester


class Solution:
    def _isvalid(self, i, j, c):
        for k in range(9):
            if self.board[i][k] == c:
                return False
            if self.board[k][j] == c:
                return False
            if self.board[k // 3 + i // 3 * 3][k % 3 + j // 3 * 3] == c:
                return False
        return True

    def _solve(self, start_row=0) -> bool:
        for i in range(start_row, 9):
            for j in range(9):
                if self.board[i][j] != ".":
                    continue
                for c in string.digits[1:]:
                    if not self._isvalid(i, j, c):
                        continue
                    self.board[i][j] = c
                    if self._solve(i):
                        return True
                    else:
                        self.board[i][j] = "."
                return False
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self._solve()
        return board


t = Tester(Solution())

t.test(
    [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
    ],
    [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ],
)

t.report()
