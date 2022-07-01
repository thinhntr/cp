# https://leetcode.com/contest/biweekly-contest-73/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/
from typing import List
from tester import Tester


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = {}
        for start, end in edges:
            if start in graph:
                graph[start].append(end)
            else:
                graph[start] = [end]

        ancestors = [set() for _ in range(n)]
        for start in graph:
            stack = graph[start][:]
            visited = set(stack)
            while stack:
                end = stack.pop()
                ancestors[end].add(start)
                visited.add(end)
                if end not in graph:
                    continue
                for predecesor in graph[end]:
                    if predecesor in visited:
                        continue
                    stack.append(predecesor)
        return list(map(sorted, ancestors))


t = Tester(Solution())

t.test(
    [[9], [], [5, 7, 8], [8], [], [], [1], [8], [], []],
    10,
    [[5, 2], [8, 7], [7, 2], [8, 3], [1, 6], [9, 0]],
)

t.test(
    [[2, 4, 5], [0, 2, 4, 5], [4], [0, 1, 2, 4, 5], [], [2, 4]],
    6,
    [
        [0, 3],
        [5, 0],
        [2, 3],
        [4, 3],
        [5, 3],
        [1, 3],
        [2, 5],
        [0, 1],
        [4, 5],
        [4, 2],
        [4, 0],
        [2, 1],
        [5, 1],
    ],
)

t.test(
    [[], [], [], [0, 1], [0, 2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3]],
    8,
    [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]],
)

t.test(
    [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]],
    5,
    [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]],
)

t.report()
