# https://leetcode.com/problems/maximum-total-importance-of-roads/
from collections import Counter
from typing import List

from tester import Tester


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        deg = Counter()
        for a, b in roads:
            deg[a] += 1
            deg[b] += 1
        cities = sorted(zip(deg.values(), deg.keys()), reverse=True)
        for i, (_, k) in zip(range(n, 0, -1), cities):
            deg[k] = i

        total = 0
        for a, b in roads:
            total += deg[a] + deg[b]
        return total


t = Tester(Solution())

t.test(43, 5, [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]])
t.test(20, 5, [[0,3],[2,4],[1,3]])
t.test(9, 5, [[0, 1]])
t.report()
