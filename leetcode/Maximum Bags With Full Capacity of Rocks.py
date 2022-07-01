# https://leetcode.com/contest/weekly-contest-294/problems/maximum-bags-with-full-capacity-of-rocks/
from typing import List

from tester import Tester


class Solution:
    def maximumBags(
        self, capacity: List[int], rocks: List[int], additionalRocks: int
    ) -> int:
        missing = sorted(cap - rock for cap, rock in zip(capacity, rocks))
        count = 0
        for m in missing:
            if additionalRocks < m:
                break
            additionalRocks -= m
            count += 1
        return count


t = Tester(Solution())

t.test(13, [54,18,91,49,51,45,58,54,47,91,90,20,85,20,90,49,10,84,59,29,40,9,100,1,64,71,30,46,91],
[14,13,16,44,8,20,51,15,46,76,51,20,77,13,14,35,6,34,34,13,3,8,1,1,61,5,2,15,18],
77)
t.test(3, capacity=[2, 3, 4, 5], rocks=[1, 2, 4, 4], additionalRocks=2)
t.test(3, capacity=[10, 2, 2], rocks=[2, 2, 0], additionalRocks=100)

t.report()
