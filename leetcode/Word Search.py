# https://leetcode.com/problems/word-search/
from typing import List

from tester import Tester


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def backtrack(word_idx, r, c):
            if word_idx == len(word):
                return True

            for dr, dc in directions:
                idx = nr, nc = r + dr, c + dc
                if (
                    idx in visited
                    or not (0 <= nr < m)
                    or not (0 <= nc < n)
                    or board[nr][nc] != word[word_idx]
                ):
                    continue

                visited.add(idx)
                if backtrack(word_idx + 1, nr, nc):
                    return True
                visited.remove(idx)
            return False

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    visited = {(r, c)}
                    if backtrack(1, r, c):
                        return True
        return False


t = Tester(Solution())

t.test(True, [["a"]], "a")
t.test(
    True, [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"
)
t.test(True, [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE")
t.test(
    False, [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"
)

t.report()
