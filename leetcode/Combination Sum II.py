# https://leetcode.com/problems/combination-sum-ii/
from icecream import ic
from tester import Tester
from typing import List


class Solution:
    def combinations(self, start, target):
        if not target:
            self.result.append(self.comb[:])
            return

        for i, candidate in enumerate(self.candidates[start:], start):
            if candidate > target:
                return
            if i and candidate == self.candidates[i - 1] and i > start:
                continue
            self.comb.append(candidate)
            self.combinations(i + 1, target - candidate)
            self.comb.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.n = len(candidates)
        self.candidates = candidates
        self.comb = []
        self.result = []
        self.combinations(0, target)

        return self.result


t = Tester(Solution())

t.test([[1]], [1, 1, 1, 1], 1)
t.test([[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]], [10, 1, 2, 7, 6, 1, 5], 8)
t.test([[1, 2, 2], [5]], [2, 5, 2, 1, 2], 5)

t.report()
