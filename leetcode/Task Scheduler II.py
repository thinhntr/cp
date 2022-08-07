# https://leetcode.com/problems/task-scheduler-ii/
from typing import List

from tester import Tester


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        day = 0
        last_day = {}
        for task in tasks:
            day += 1
            if task in last_day:
                delta = space - (day - last_day[task] - 1)
                day += delta if delta > 0 else 0
            last_day[task] = day
        return day


t = Tester(Solution())

t.test(6, [5, 8, 8, 5], 2)
t.test(9, [1, 2, 1, 2, 3, 1], 3)
t.test(1, [5], 100)
t.test(2, [5, 2], 1)

t.report()
