# https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/
from typing import List

from tester import Tester


class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades) - 1 
        prev = 1
        while n >= prev + 1:
            n -= (prev+1)
            prev += 1
        return prev



t = Tester(Solution())

t.test(3, [47,2,16,17,41,4,38,23,47])
t.test(3, [10,6,12,7,3,5])
t.test(1, [8,8])

t.report()
