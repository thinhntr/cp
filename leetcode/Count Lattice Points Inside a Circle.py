# https://leetcode.com/contest/weekly-contest-290/problems/count-lattice-points-inside-a-circle/
from typing import List

from tester import Tester


class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        visited = set()
        for x, y, r in circles:
            for xi in range(-r, r + 1):
                for yi in range(-r, r + 1):
                    if xi * xi + yi * yi <= r * r:
                        visited.add((xi + x, yi + y))
        return len(visited)


t = Tester(Solution())

t.test(5, [[2, 2, 1]])
t.test(16, [[2, 2, 2], [3, 4, 1]])

t.report()
