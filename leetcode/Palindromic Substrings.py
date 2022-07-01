# https://leetcode.com/problems/palindromic-substrings/submissions/
from typing import List

from tester import Tester

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n):
            count += 1
            l, r = i - 1, i + 1
            while 0 <= l and r < n:
                if s[l] != s[r]:
                    break
                count += 1
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while 0 <= l and r < n:
                if s[l] != s[r]:
                    break
                count += 1
                l -= 1
                r += 1
        return count

t = Tester(Solution())

t.test(6, "aaa")
t.test(3, "abc")
t.test(6, "adda")
t.test(3, "vv")

t.report()