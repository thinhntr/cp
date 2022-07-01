# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
from functools import reduce
from operator import add
from typing import List

from tester import Tester


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return reduce(add, map(lambda i: not len(str(i)) & 1, nums), 0)


t = Tester(Solution())

t.test(2, [12, 345, 2, 6, 7896])
t.test(1, [555, 901, 482, 1771])

t.report()
