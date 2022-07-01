# https://leetcode.com/problems/concatenation-of-array/
from typing import List

from tester import Tester

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

t = Tester(Solution())

t.test([1,2,1,1,2,1], [1,2,1])
t.test([1,3,2,1,1,3,2,1], [1,3,2,1])

t.report()