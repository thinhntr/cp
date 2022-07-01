# https://leetcode.com/problems/evaluate-reverse-polish-notation/
from operator import add, mul, sub
from typing import List

from tester import Tester


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        val = 0
        stack = []
        ops = {"+": add, "-": sub, "*": mul, "/": lambda a, b: int(a / b)}
        for token in tokens:
            if token in ops:
                op = ops[token]
                b, a = stack.pop(), stack.pop()
                val = op(a, b)
            else:
                val = int(token)
            stack.append(val)
        return val


t = Tester(Solution())

t.test(1, ["4", "3", "-"])
t.test(22, ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
t.test(6, ["4", "13", "5", "/", "+"])
t.test(9, ["2", "1", "+", "3", "*"])

t.report()
