# https://leetcode.com/contest/weekly-contest-290/problems/intersection-of-multiple-arrays/
from typing import List

from tester import Tester

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = set(nums[0])
        for num in nums:
            res &= set(num)
        return sorted(list(res))

t = Tester(Solution())

t.test()

t.report()