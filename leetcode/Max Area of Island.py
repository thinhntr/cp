# https://leetcode.com/problems/max-area-of-island/

from typing import List
from collections import deque

steps = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def is_valid_cell(image, visited, discovered, new_cell, nr, nc) -> bool:
    new_r, new_c = new_cell
    return (0 <= new_r < nr
            and 0 <= new_c < nc
            and image[new_r][new_c] == 1
            and new_cell not in discovered
            and new_cell not in visited)


def next_cells(image, visited, discovered, old_cell, nr, nc) -> deque:
    results = deque()
    for step in steps:
        new_cell = old_cell[0] + step[0], old_cell[1] + step[1]
        if is_valid_cell(image, visited, discovered, new_cell, nr, nc):
            results.append(new_cell)
            discovered.add(new_cell)
    return results


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        nr = len(grid)
        nc = len(grid[0])

        visited = set()

        for r in range(nr):
            for c in range(nc):
                current_cell = (r, c)
                if not grid[r][c] or current_cell in visited:
                    continue

                visited.add(current_cell)
                discovered = set()
                current_area = 1
                neighbors = next_cells(grid, visited, discovered, current_cell, nr, nc)

                while neighbors:
                    neighbor = neighbors.popleft()
                    discovered.remove(neighbor)
                    visited.add(neighbor)

                    current_area += 1

                    for new_neighbor in next_cells(grid, visited, discovered, neighbor, nr, nc):
                        neighbors.append(new_neighbor)

                max_area = max(max_area, current_area)

        return max_area


grid1 = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

grid2 = [[0, 0, 0, 0, 0, 0, 0, 0]]

grid3 = [[1, 1, 0, 0, 0], 
         [1, 1, 0, 0, 0], 
         [0, 0, 0, 1, 1], 
         [0, 0, 0, 1, 1]]

solution = Solution()

# assert solution.maxAreaOfIsland(grid1) == 6
# assert solution.maxAreaOfIsland(grid2) == 0
assert solution.maxAreaOfIsland(grid3) == 4
