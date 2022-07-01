# https://leetcode.com/problems/find-eventual-safe-states/
from typing import List
from tester import Tester


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """My Solution
        """
        n = len(graph)
        not_ok = set(range(n))

        def dfs(u, visited):
            if u in visited:
                return False
            visited.add(u)
            for v in graph[u]:
                if v in not_ok and (v in visited or not dfs(v, visited)):
                    return False
            not_ok.remove(u)
            return True

        for u in range(n):
            if u in not_ok:
                dfs(u, set())

        return [i for i in range(n) if i not in not_ok]

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """NeetCode's Solution
        """
        is_ok = {}
        def dfs(u):
            if u in is_ok:
                return is_ok[u]
            is_ok[u] = False
            for v in graph[u]:
                if not dfs(v):
                    return False
            is_ok[u] = True
            return True

        return [u for u in range(len(graph)) if dfs(u)]


t = Tester(Solution())

t.test(
    [5, 8, 9],
    [
        [1, 3, 4, 5, 7, 9],
        [1, 3, 8, 9],
        [3, 4, 5, 8],
        [1, 8],
        [5, 7, 8],
        [8, 9],
        [7, 8, 9],
        [3],
        [],
        [],
    ],
)
t.test([0, 1, 2, 3, 4], [[], [0, 2, 3, 4], [3], [4], []])
t.test([0, 1, 2], [[2], [2], []])
t.test([0, 1, 2], [[2], [0, 2], []])
t.test([2, 4, 5, 6], [[1, 2], [2, 3], [5], [0], [5], [], []])
t.test([], [[1], [0]])
t.test([4], [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []])

t.report()
