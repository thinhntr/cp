# https://leetcode.com/problems/daily-temperatures/
from typing import List
from tester import Tester


class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = [0] * len(temps)
        stack = []
        for i in range(len(temps)):
            while stack and temps[stack[-1]] < temps[i]:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res


t = Tester(Solution())

t.test([1, 1, 4, 2, 1, 1, 0, 0], [73, 74, 75, 71, 69, 72, 76, 73])
t.test([1, 1, 1, 0], [30, 40, 50, 60])
t.test([1, 1, 0], [30, 60, 90])

t.report()
