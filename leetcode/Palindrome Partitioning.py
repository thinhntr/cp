# https://leetcode.com/problems/palindrome-partitioning/
from pydoc import ispackage
from typing import List

from tester import Tester


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(start, end):
            end -= 1
            while start < end:
                if s[start] != s[end]:
                    return False
                start, end = start + 1, end - 1
            return True

        def split(start, end) -> List[List[int]]:
            res = []

            for mid in range(start + 1, end + 1):
                if not is_palindrome(start, mid):
                    continue
                tmp = split(mid, end)
                substring = s[start:mid]
                if mid == end:
                    res.append([substring])
                for item in tmp:
                    res.append([substring, *item])
            return res

        return split(0, len(s))


t = Tester(Solution())

t.test([["a", "b", "a"], ["aba"]], "aba")
t.test([["a", "a", "bb"], ["a", "a", "b", "b"], ["aa", "bb"], ["aa", "b", "b"]], "aabb")
t.test([["a", "a", "b"], ["aa", "b"]], "aab")
t.test([["a"]], "a")

t.report()
