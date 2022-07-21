# https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/
from collections import Counter
from functools import reduce
from math import gcd
from typing import List

from tester import Tester


class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        greatest_common = reduce(gcd, numsDivide)
        counter = sorted(Counter(nums).items())
        num_delete = 0
        for key, freq in counter:
            if greatest_common % key == 0:
                return num_delete
            num_delete += freq
        return -1


t = Tester(Solution())

t.test(-1, [4, 3, 6], [8, 2, 6, 10])
t.test(2, [2, 3, 2, 4, 3], [9, 6, 9, 3, 15])

t.report()
