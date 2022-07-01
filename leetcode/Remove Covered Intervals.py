# https://leetcode.com/problems/remove-covered-intervals/
from typing import List
from tester import Tester


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x: (x[0], -x[1]))
        end = intervals[0][1]
        for interval in intervals[1:]:
            if interval[1] <= end:
                n -= 1
            else:
                end = interval[1]
        return n


t = Tester(Solution())

t.test(1, [[1, 2], [1, 4], [3, 4]])
t.test(2, [[1, 4], [3, 6], [2, 8]])
t.test(1, [[1, 4], [2, 3]])

t.report()
import string

string.ascii_lowercase
