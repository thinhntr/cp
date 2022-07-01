# https://leetcode.com/problems/combination-sum/
from collections import deque
from typing import List
from tester import Tester


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = deque()
        n = len(candidates)

        def dfs(index, combination, target):
            if not target:
                result.append(combination)
            for i in range(index, n):
                if target < candidates[i]:
                    continue
                dfs(i, combination + deque([candidates[i]]), target - candidates[i])

        dfs(0, deque(), target)
        return list(map(lambda it: list(it), result))


t = Tester(Solution())

t.test([[2, 2, 3], [7]], [2, 3, 6, 7], 7)
t.test([[2, 2, 2, 2], [2, 3, 3], [3, 5]], [2, 3, 5], 8)
t.test([], [2], 1)

t.report()
