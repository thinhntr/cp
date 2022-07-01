# https://leetcode.com/problems/compare-version-numbers/
from typing import List
from tester import Tester


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [it.lstrip("0") for it in version1.split(".")]
        v2 = [it.lstrip("0") for it in version2.split(".")]
        lenv1 = len(v1)
        lenv2 = len(v2)
        for i in range(max(lenv1, lenv2)):
            r1 = "0" if i >= lenv1 else v1[i]
            r2 = "0" if i >= lenv2 else v2[i]
            if len(r1) < len(r2):
                r1 = "0" * (len(r2) - len(r1)) + r1
            elif len(r2) < len(r1):
                r2 = "0" * (len(r1) - len(r2)) + r2
            if r1 < r2:
                return -1
            elif r1 > r2:
                return 1
        return 0


t = Tester(Solution())

t.test(0, "1.0", "1.0.0")
t.test(-1, "1.2", "1.10")

t.report()
