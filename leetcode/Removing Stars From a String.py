# 
from typing import List

from tester import Tester

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == "*":
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)

t = Tester(Solution())

t.test("lecoe", "leet**cod*e")
t.test("", "erase*****")

t.report()