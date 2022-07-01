# https://leetcode.com/problems/rotting-oranges/
from typing import List

from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nrow = len(grid)
        ncol = len(grid[0])

        # Find rotten oranges' locations
        rottens = []
        found_fresh = False
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 1:
                    found_fresh = True
                elif grid[i][j] == 2:
                    rottens.append((i, j))

        # Return if not rotten oranges if found
        if not rottens:
            if found_fresh:
                return -1
            return 0

        # Propagate rotten
        depth = {}
        queue = deque()
        for rotten in rottens:
            depth[rotten] = 0
            queue.append(rotten)
        visited = set()
        steps = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue:
            cell = queue.popleft()
            visited.add(cell)

            grid[cell[0]][cell[1]] = 2

            for step in steps:
                new_cell = cell[0] + step[0], cell[1] + step[1]
                r, c = new_cell
                if (not (0 <= r < nrow and 0 <= c < ncol and grid[r][c] == 1)
                        or new_cell in visited):
                    continue
                depth[new_cell] = depth[cell] + 1
                visited.add(new_cell)
                queue.append(new_cell)

        # check if all oranges are rotten
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j] == 1:
                    return -1

        # Final result
        return depth[cell]


solution = Solution()


def check(a, b):
    result = solution.orangesRotting(a)
    assert result == b


check([[2, 2], [1, 1], [0, 0], [2, 0]], 1)
check([[2, 1, 1], [1, 1, 1], [0, 1, 2]], 2)
check([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4)
check([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1)
check([[0, 2]], 0)
check([[1]], -1)
check([[0]], 0)
