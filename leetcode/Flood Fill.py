# https://leetcode.com/problems/flood-fill/

from typing import List
from collections import deque

steps = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def is_valid_cell(image, visited, orgColor, new_cell, nr, nc) -> bool:
    new_r, new_c = new_cell
    return (0 <= new_r < nr
            and 0 <= new_c < nc
            and image[new_r][new_c] == orgColor
            and new_cell not in visited)


def next_cells(image, visited, orgColor, old_cell, nr, nc) -> deque:
    results = deque()
    for step in steps:
        new_cell = old_cell[0] + step[0], old_cell[1] + step[1]
        if is_valid_cell(image, visited, orgColor, new_cell, nr, nc):
            results.append(new_cell)
    return results


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        nr = len(image)
        nc = len(image[0])

        orgColor = image[sr][sc]
        image[sr][sc] = newColor

        start_cell = (sr, sc)
        visited = {start_cell}
        neighbors = next_cells(image, visited, orgColor, start_cell, nr, nc)

        while neighbors:
            neighbor = neighbors.popleft()
            image[neighbor[0]][neighbor[1]] = newColor

            visited.add(neighbor)
            for new_neighbor in next_cells(image, visited, orgColor, neighbor, nr, nc):
                neighbors.append(new_neighbor)
        
        return image


solution = Solution()
assert solution.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == [
    [2, 2, 2], [2, 2, 0], [2, 0, 1]]
assert solution.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 2) == [[2, 2, 2], [2, 2, 2]]
