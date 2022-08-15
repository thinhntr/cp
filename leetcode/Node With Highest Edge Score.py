# https://leetcode.com/problems/node-with-highest-edge-score/
from typing import List

from tester import Tester


class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        scores = [0] * len(edges)
        for start, end in enumerate(edges):
            scores[end] += start
        return scores.index(max(scores))


t = Tester(Solution())

t.test(7, [1, 0, 0, 0, 0, 7, 7, 5])
t.test(0, [2, 0, 0, 2])

t.report()
