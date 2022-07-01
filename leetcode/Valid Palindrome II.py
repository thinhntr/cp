# https://leetcode.com/problems/valid-palindrome-ii/
from typing import List
from tester import Tester


class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r and s[l] == s[r]:
            l, r = l + 1 ,r - 1

        if l >= r:
            return True
        # Case 1: Remove left character
        l1, r1 = l + 1, r
        while l1 <= r1 and s[l1] == s[r1]:
            l1, r1 = l1 + 1, r1 - 1
        if l1 >= r1:
            return True

        # Case 2: Remove right character
        l2, r2 = l, r - 1
        while l2 <= r2 and s[l2] == s[r2]:
            l2, r2 = l2 + 1, r2 - 1

        return l2 >= r2


t = Tester(Solution())

t.test(True, "cuucu")
t.test(False, "tebbem")
t.test(True, "aba")
t.test(True, "abca")
t.test(False, "abc")
t.test(True, "acddcea")
t.test(True, "acdcea")
t.test(False, "acdfcea")
t.test(False, "acd")
t.test(True, "cbbcc")
t.test(True, "ccbbc")
t.test(
    True,
    "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga",
)

t.report()
