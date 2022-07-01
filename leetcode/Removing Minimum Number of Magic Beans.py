# https://leetcode.com/problems/removing-minimum-number-of-magic-beans/
from itertools import accumulate
from operator import add
from typing import List
from tester import Tester


class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.append(0)
        beans.sort()
        *beans_accum, total = accumulate(beans, add)
        n = len(beans_accum)
        for i in range(n):
            total -= (beans[i + 1] - beans[i]) * (n - i)
            beans_accum[i] += total
        return min(beans_accum)


t = Tester(Solution())

t.test(4, [4, 1, 6, 5])
t.test(7, [2, 10, 3, 2])
t.test(14, [10, 9, 8, 6, 5, 1])

t.report()
