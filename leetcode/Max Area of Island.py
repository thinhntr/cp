# https://leetcode.com/problems/max-area-of-island/
from typing import List, Set, Tuple

from tester import Tester


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """Recursive DFS"""
        m, n = len(grid), len(grid[0])
        visited: Set[Tuple[int, int]] = set()

        def dfs(i, j):
            if (
                (i, j) in visited
                or i < 0
                or i >= m
                or j < 0
                or j >= n
                or not grid[i][j]
            ):
                return 0
            visited.add((i, j))
            area = 1
            area += dfs(i + 1, j)
            area += dfs(i - 1, j)
            area += dfs(i, j + 1)
            area += dfs(i, j - 1)
            return area

        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))
        return result

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """Iterative DFS"""
        m, n = len(grid), len(grid[0])
        visited: Set[Tuple[int, int]] = set()
        result = 0

        for i in range(m):
            for j in range(n):
                stack = [(i, j)]
                area = 0
                while stack:
                    ci, cj = stack.pop()
                    if (
                        (ci, cj) in visited
                        or ci < 0
                        or ci >= m
                        or cj < 0
                        or cj >= n
                        or not grid[ci][cj]
                    ):
                        continue
                    area += 1
                    visited.add((ci, cj))
                    stack.append((ci + 1, cj))
                    stack.append((ci - 1, cj))
                    stack.append((ci, cj + 1))
                    stack.append((ci, cj - 1))
                result = max(result, area)

        return result

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """Disjoin Set"""
        m, n = len(grid), len(grid[0])
        parent = [i for i in range(m * n)]
        size = [0] * (m * n)

        def hash_indices(i, j):
            return i * n + j

        def find_set(u):
            if u == parent[u]:
                return u
            parent[u] = find_set(parent[u])
            return parent[u]

        def union_sets(u, v):
            a = find_set(u)
            b = find_set(v)
            if a != b:
                if size[a] < size[b]:
                    a, b = b, a
                parent[b] = a
                size[a] += size[b]

        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    continue
                u = hash_indices(i, j)
                size[u] = 1

                if i > 0 and grid[i - 1][j]:
                    v = hash_indices(i - 1, j)
                    union_sets(u, v)

                if j > 0 and grid[i][j - 1]:
                    v = hash_indices(i, j - 1)
                    union_sets(u, v)

        return max(size)


t = Tester(Solution())

t.test(0, [[0, 0, 0, 0, 0, 0, 0, 0]])

t.test(4, [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]])

t.test(
    6,
    [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ],
)

t.report()
