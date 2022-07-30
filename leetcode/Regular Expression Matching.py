# https://leetcode.com/problems/regular-expression-matching/

from functools import lru_cache

from tester import Tester


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        r = len(p) - 1
        ops = []
        while r >= 0:
            l = r - 1 if p[r] == "*" else r
            ops.append(p[l : r + 1])
            r = l - 1
        ops = ops[::-1]

        lo = len(ops)
        ls = len(s)

        @lru_cache
        def check(i, j):
            if j == lo:
                return i == ls

            if len(ops[j]) == 1:
                return (
                    i < ls and (s[i] == ops[j] or ops[j] == ".") and check(i + 1, j + 1)
                )

            if i == ls:
                return check(i, j + 1)

            if (s[i] == ops[j][0] or ops[j][0] == ".") and check(i + 1, j):
                return True

            return check(i, j + 1)

        return check(0, 0)


t = Tester(Solution())

t.test(False, "a", ".*..a*")
t.test(True, "abcddef", "a.*d*")
t.test(False, "abcddef", "a.*d*j")
t.test(True, "ab", ".*")
t.test(True, "abcdefg", "a.*d*g")
t.test(False, "abcdefg", "a.*d*gf")
t.test(True, "aa", "a*")
t.test(True, "adlkcc", "a.*.*")
t.test(False, "aa", "a")
t.test(False, "abcdef", "abcd*")
t.test(True, "abcddefj", "a.*d*j")
t.test(True, "abbbbb", "ab*")
t.test(False, "abbbc", "ab*")
t.test(True, "abcdef", "d*abcd.*")
t.test(True, "dddef", "d*ef")

t.report()
