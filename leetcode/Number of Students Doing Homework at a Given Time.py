# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/
from functools import reduce
from typing import List

from tester import Tester

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return reduce(lambda a, b: a + (b[0] <= queryTime <= b[1]), zip(startTime, endTime), 0)

t = Tester(Solution())

t.test(1, startTime = [1,2,3], endTime = [3,2,7], queryTime = 4)
t.test(1, startTime = [4], endTime = [4], queryTime = 4)

t.report()