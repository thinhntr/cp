# https://leetcode.com/problems/n-queens/


from typing import List


class Solution(object):
    def toStrArr(self, board: List[List[int]]) -> List[str]:
        new_board: List[str] = []
        nrow = len(board)
        for row in board:
            dot_count = 0
            for i in row:
                if i == 1:
                    break
                dot_count += 1
            left_dots = f"{'.' * dot_count}"
            q = f"{'Q' * (1 if dot_count < nrow else 0)}"
            right_dots = f"{'.' * (nrow - dot_count - 1)}"
            new_board.append(f"{left_dots}{q}{right_dots}")
        return new_board

    def checkRow(self, board: List[List[int]], x: int, y: int) -> bool:
        return not any(board[x])

    def checkLeftDiag(self, board: List[List[int]], x: int, y: int) -> bool:
        ncol = len(board)
        start_x = x - (x if x < y else y)
        start_y = y - (y if y < x else x)
        elem_count = ncol - max(start_x, start_y)
        leftDiag = [board[start_x + i][start_y + i] for i in range(elem_count)]
        return not any(leftDiag)

    def checkRightDiag(self, board: List[List[int]], x: int, y: int) -> bool:
        ncol = len(board)
        d = 0
        while x - d >= 0 and y + d < ncol:
            if board[x - d][y + d] == 1:
                return False
            d += 1
        d = 0
        while x + d < ncol and y - d >= 0:
            if board[x + d][y - d] == 1:
                return False
            d += 1
        return True


    def checkPosition(self, board: List[List[int]], x: int, y: int) -> bool:
        """Return True if there is no Queen attacking current position"""
        return (
            self.checkRow(board, x, y)
            and self.checkLeftDiag(board, x, y)
            and self.checkRightDiag(board, x, y)
        )

    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [[0] * n for _ in range(n)]
        row_pointers = [0] * n
        current_col = 0
        configs: List[List[str]] = []
        while current_col >= 0:
            y = current_col
            x = row_pointers[current_col] if current_col < n else 0
            if y == n:
                configs.append(self.toStrArr(board))
                current_col -= 1
            elif x == n:
                row_pointers[current_col] = 0
                current_col -= 1
            elif board[x][y] == 1:
                board[x][y] = 0
                row_pointers[current_col] += 1
                continue
            elif self.checkPosition(board, x, y):
                board[x][y] = 1
                current_col += 1
                continue
            else:
                row_pointers[current_col] += 1

        return configs


if __name__ == "__main__":
    s = Solution()
    strs = s.solveNQueens(3)
    for str_ in strs:
        print(*str_, sep='\n')
        print('-'*10)