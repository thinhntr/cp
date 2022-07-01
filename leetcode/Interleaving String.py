# https://leetcode.com/problems/interleaving-string/
from functools import cache

from tester import Tester


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = map(len, (s1, s2, s3))
        if n1 + n2 != n3:
            return False

        @cache
        def helper(i1, i2):
            if i1 + i2 == n3:
                return True

            return (
                i1 < n1
                and s1[i1] == s3[i1 + i2]
                and helper(i1 + 1, i2)
                or i2 < n2
                and s2[i2] == s3[i1 + i2]
                and helper(i1, i2 + 1)
            )

        return helper(0, 0)


t = Tester(Solution())

t.test(True, "aabcc", "dbbca", "aadbbcbcac")
t.test(False, "aabcc", "dbbca", "aadbbbaccc")
t.test(True, "", "", "")

t.report()
