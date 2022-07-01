# https://leetcode.com/contest/weekly-contest-288/problems/minimize-result-by-adding-parentheses-to-expression/
from typing import List
from tester import Tester


class Solution:
    def minimizeResult(self, expression: str) -> str:
        n1, n2 = expression.split("+")
        l1, l2 = len(n1), len(n2)

        def eval(s1, s2):
            a = int(n1[:s1]) if s1 else 1
            b = int(n1[s1:]) if s1 < l1 else 0
            c = int(n2[:s2]) if s2 else 0
            d = int(n2[s2:]) if s2 < l2 else 1
            return a * (b + c) * d

        m1, m2 = 0, l2
        minimal = eval(m1, m2)
        for s1 in range(l1):
            for s2 in range(1, l2 + 1):
                tmp = eval(s1, s2)
                if tmp < minimal:
                    m1, m2 = s1, s2
                    minimal = tmp

        return f"{n1[:m1]}({n1[m1:]}+{n2[:m2]}){n2[m2:]}"


t = Tester(Solution())

t.test("(1+1)", "1+1")
t.test("(393+997)397", "393+997397")
t.test("4(5+4)1", "45+41")
t.test("(999+999)", "999+999")
t.test("2(47+38)", "247+38")
t.test("1(2+3)4", "12+34")

t.report()
