# https://leetcode.com/problems/network-delay-time/
from collections import deque
from typing import List
from tester import Tester
from heapq import heappop, heappush


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v, t in times:
            graph[u].append((v, t))

        dist = [float("inf")] * (n + 1)
        dist[k] = 0
        pq = [(0, k)]
        while pq:
            _, u = heappop(pq)
            for v, t in graph[u]:
                if dist[v] > dist[u] + t:
                    dist[v] = dist[u] + t
                    heappush(pq, (dist[v], v))
        res = max(dist[1:])
        return res if res != float("inf") else -1


t = Tester(Solution())

t.test(
    31,
    [
        [3, 5, 78],
        [2, 1, 1],
        [1, 3, 0],
        [4, 3, 59],
        [5, 3, 85],
        [5, 2, 22],
        [2, 4, 23],
        [1, 4, 43],
        [4, 5, 75],
        [5, 1, 15],
        [1, 5, 91],
        [4, 1, 16],
        [3, 2, 98],
        [3, 4, 22],
        [5, 4, 31],
        [1, 2, 0],
        [2, 5, 4],
        [4, 2, 51],
        [3, 1, 36],
        [2, 3, 59],
    ],
    5,
    5,
)
t.test(3, [[1, 2, 2], [1, 4, 1], [1, 3, 4], [4, 3, 1], [3, 5, 1]], 5, 1)
t.test(3, [[1, 2, 1], [2, 3, 2], [1, 3, 4]], 3, 1)
t.test(2, [[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2)
t.test(1, [[1, 2, 1]], 2, 1)
t.test(-1, [[1, 2, 1]], 2, 2)

t.report()
