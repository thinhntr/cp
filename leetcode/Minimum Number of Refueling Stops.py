# https://leetcode.com/problems/minimum-number-of-refueling-stops/
import heapq
from typing import List
from tester import Tester


class Solution:
    def minRefuelStops(
        self, target: int, startFuel: int, stations: List[List[int]]
    ) -> int:
        pq = []
        i = count = 0
        while startFuel < target:
            while i < len(stations) and stations[i][0] <= startFuel:
                heapq.heappush(pq, -stations[i][1])                
                i += 1
            if not pq:
                return -1
            startFuel -= heapq.heappop(pq)
            count += 1
        return count


t = Tester(Solution())

t.test(
    4,
    1000,
    299,
    [
        [13, 21],
        [26, 115],
        [100, 47],
        [225, 99],
        [299, 141],
        [444, 198],
        [608, 190],
        [636, 157],
        [647, 255],
        [841, 123],
    ],
)
t.test(
    4,
    1000,
    83,
    [
        [47, 220],
        [65, 1],
        [98, 113],
        [126, 196],
        [186, 218],
        [320, 205],
        [686, 317],
        [707, 325],
        [754, 104],
        [781, 105],
    ],
)
t.test(2, 110, 20, [[10, 10], [30, 80], [80, 20]])
t.test(2, 110, 20, [[10, 10], [20, 60], [30, 80], [80, 20]])
t.test(2, 100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]])
t.test(0, 1, 1, [])
t.test(-1, 100, 1, [[10, 100]])

t.report()
