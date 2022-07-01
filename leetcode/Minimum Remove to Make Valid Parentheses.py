#
from typing import List
from tester import Tester


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        stack = []
        valid = set(range(n))
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            if c == ")":
                if stack:
                    stack.pop()
                else:
                    valid.remove(i)
        while stack:
            valid.remove(stack.pop())
        result = (s[i] for i in range(n) if i in valid)
        return "".join(result)


t = Tester(Solution())

t.test("lee(t(c)o)de", "lee(t(c)o)de)")
t.test("ab(c)d", "a)b(c)d")
t.test("", "))((")
t.test("()", "()")

t.report()
