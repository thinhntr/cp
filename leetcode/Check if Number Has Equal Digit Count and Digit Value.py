# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/
from collections import Counter
from typing import List

from tester import Tester

class Solution:
    def digitCount(self, num: str) -> bool:
        c = Counter(num)
        for i in range(len(num)):
            if c[str(i)] != int(num[i]):
                return False
        return True

t = Tester(Solution())

t.test(True, "1210")
t.test(False, "030")

t.report()