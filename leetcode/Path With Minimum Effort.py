# https://leetcode.com/problems/path-with-minimum-effort/
from collections import defaultdict
from heapq import heappop, heappush
from typing import List

from tester import Tester


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        nrow, ncol = len(heights), len(heights[0])
        start, target = 0, nrow * ncol - 1
        efforts = defaultdict(lambda: float("inf"))
        efforts[0] = 0
        queue = [[0, start]]
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        while queue:
            e, u = heappop(queue)
            i, j = u // ncol, u % ncol
            for direction in directions:
                tmpi = i + direction[0]
                tmpj = j + direction[1]
                if not (0 <= tmpi < nrow) or not (0 <= tmpj < ncol):
                    continue
                v = tmpi * ncol + tmpj
                diff = abs(heights[i][j] - heights[tmpi][tmpj])
                tmpe = min(efforts[v], max(e, diff))
                if tmpe < efforts[v]:
                    heappush(queue, (tmpe, v))
                    efforts[v] = tmpe

        return efforts[target]


t = Tester(Solution())

t.test(2, [[1, 2, 2], [3, 8, 2], [5, 3, 5]])
t.test(1, [[1, 2, 3], [3, 8, 4], [5, 3, 5]])
t.test(
    0,
    [
        [1, 2, 1, 1, 1],
        [1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1],
        [1, 2, 1, 2, 1],
        [1, 1, 1, 2, 1],
    ],
)

t.report()
