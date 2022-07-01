# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/
from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s = Counter(s)
        t = Counter(t)
        schars = set(s.keys())
        tchars = set(t.keys())
        steps = 0
        for c in (schars | tchars):
            steps += abs(s[c] - t[c])
        return steps
