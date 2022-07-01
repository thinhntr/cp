# https://leetcode.com/problems/all-paths-from-source-to-target/
from typing import List
from collections import deque

def check_paths(paths, end):
    for i, path in enumerate(paths):
        if path[-1] != end:
            return i
    return len(paths)

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        start = 0
        end = len(graph) - 1
        paths = [[start]]
        current_idx = check_paths(paths, end)
        while current_idx != len(paths):
            current_path = paths[current_idx][:]
            current_end = current_path[-1]
            neighbors = graph[current_end]
            if len(neighbors) > 0:
                paths[current_idx] = [*current_path, neighbors[0]]
            else:
                del paths[current_idx]
            for neighbor in neighbors[1:]:
                paths.append([*current_path, neighbor])
            current_idx = check_paths(paths, end)
            # print(current_idx)
        return paths


solution = Solution()


def check(input, expected):
    output = solution.allPathsSourceTarget(input)
    assert output == expected

check([[1,2],[3],[3],[]], 
      [[0,1,3],[0,2,3]])

# [[0]]
# [[0, 1], [0, 2]]
# [[0, 1, 3], [0, 2, 3]]

check([[4,3,1],[3,2,4],[3],[4],[]], 
      [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]])

# [[0]]
# [[0, 4], [0, 3], [0, 1]]
# [[0, 4], [0, 3, 4], [0, 1, 3], [0, 1, 2], [0, 1, 4]]
# [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3], [0, 1, 4]]
# [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
print('Run here')
solution.allPathsSourceTarget([[4,3,1],[3,2,4],[],[4],[]])