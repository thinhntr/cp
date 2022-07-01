# https://leetcode.com/problems/01-matrix/
from typing import List

from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        nrow = len(mat)
        ncol = len(mat[0])

        # Find zeros' locations
        zeros = deque()
        for i in range(nrow):
            for j in range(ncol):
                if mat[i][j] == 0:
                    zeros.append((i, j))

        # Find nearest ones
        depth = {}
        queue = deque()
        for zero in zeros:
            depth[zero] = 0
            queue.append(zero)
        visited = set()
        steps = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while queue:
            cell = queue.popleft()
            visited.add(cell)

            mat[cell[0]][cell[1]] = depth[cell]

            for step in steps:
                new_cell = cell[0] + step[0], cell[1] + step[1]
                r, c = new_cell
                if (not (0 <= r < nrow and 0 <= c < ncol and mat[r][c] != 0)
                        or new_cell in visited):
                    continue
                depth[new_cell] = depth[cell] + 1
                visited.add(new_cell)
                queue.append(new_cell)

        return mat
    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # for i i
        top_val = mat[i][j]


solution = Solution()


def check(a, b):
    result = solution.updateMatrix(a)
    assert b == result


check([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [0, 0, 0]])

check([[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[0, 0, 0], [0, 1, 0], [1, 2, 1]])
