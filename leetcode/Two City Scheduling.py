# https://leetcode.com/problems/two-city-scheduling/
from typing import List
from tester import Tester
from operator import itemgetter
from functools import cmp_to_key
from icecream import ic


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(map(lambda cost: [cost[0] - cost[1], *cost], costs))
        m = len(costs) // 2
        a_left = sum(map(itemgetter(1), costs[:m]))
        b_right = sum(map(itemgetter(2), costs[m:]))
        return a_left + b_right


t = Tester(Solution())

t.test(90, [[10, 10], [10, 20], [30, 30], [40, 40]])
t.test(110, [[10, 20], [30, 200], [400, 50], [30, 20]])
t.test(1859, [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]])
t.test(
    3086,
    [
        [515, 563],
        [451, 713],
        [537, 709],
        [343, 819],
        [855, 779],
        [457, 60],
        [650, 359],
        [631, 42],
    ],
)

t.report()
