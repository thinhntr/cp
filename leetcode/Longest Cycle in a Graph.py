# https://leetcode.com/problems/longest-cycle-in-a-graph/
from typing import List

from tester import Tester


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        def dfs(node, idx) -> int:
            if node in mapping:
                return idx - mapping[node]
            if node not in unvisited:
                return -1
            unvisited.remove(node)
            mapping[node] = idx
            return dfs(edges[node], idx + 1)

        unvisited = set(range(len(edges)))
        result = -1
        while unvisited:
            node = unvisited.pop()
            unvisited.add(node)
            mapping = {}
            result = max(result, dfs(node, 1))
        return result


t = Tester(Solution())

t.test(3, [3, 3, 4, 2, 3])
t.test(-1, [-1, 4, -1, 2, 0, 4])
t.test(-1, [2, -1, 3, 1])
t.test(3, [4, 3, 3, 4, 7, 2, 3, 3])

t.report()
