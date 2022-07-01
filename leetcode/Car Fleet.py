# https://leetcode.com/problems/car-fleet/
from typing import List

from tester import Tester


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        count = 0
        np, nv = target, float('inf')
        for p, v in sorted(zip(position, speed), reverse=True):
            if v <= nv or target < v * (np - p) / (v - nv) + p:
                np = p
                nv = v
                count += 1
        return count


t = Tester(Solution())

t.test(3, target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3])
t.test(1, target=10, position=[3], speed=[3])
t.test(1, target=100, position=[0, 2, 4], speed=[4, 2, 1])

t.report()
