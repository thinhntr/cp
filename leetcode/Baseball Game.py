# https://leetcode.com/problems/baseball-game/      
from typing import List
from tester import Tester

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for op in ops:
            if op == "D":
                stack.append(stack[-1] * 2)
            elif op == "C":
                stack.pop()
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)

t = Tester(Solution())

t.test(30, ["5","2","C","D","+"])
t.test(27, ["5","-2","4","C","D","9","+","+"])

t.report()