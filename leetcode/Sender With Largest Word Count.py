# https://leetcode.com/problems/sender-with-largest-word-count/
from collections import Counter
from typing import List

from tester import Tester

class Solution:
    def largestWordCount(self, M: List[str], S: List[str]) -> str:
        c = Counter()
        res = ""
        for m, s in zip(M, S):
            c[s] += m.count(" ") + 1
            if c[res] < c[s] or c[res] == c[s] and res < s:
                res = s
        return res

t = Tester(Solution())

t.test("Charlie", ["How is leetcode for everyone","Leetcode is useful for practice"], ["Bob","Charlie"])
t.test("Alice", ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"], ["Alice","userTwo","userThree","Alice"])

t.report()