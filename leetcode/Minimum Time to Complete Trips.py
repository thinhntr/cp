# https://leetcode.com/problems/minimum-time-to-complete-trips/
from tester import Tester
from typing import List 

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        cal_trips = lambda t: sum(map(lambda time: t // time, time))
        mintime = 1
        maxtime = 1 << 32

        while mintime < maxtime:
            midtime = (mintime+maxtime)//2
            if cal_trips(midtime) < totalTrips:
                mintime=midtime+1
            else:
                maxtime=midtime
        return mintime

t = Tester(Solution())

t.test(3, [1,2,3],  5)
t.test(2, [2],  1)
t.test(4, [1],  4)

t.report()