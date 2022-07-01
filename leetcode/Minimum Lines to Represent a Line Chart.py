# https://leetcode.com/contest/weekly-contest-294/problems/minimum-lines-to-represent-a-line-chart/

from typing import List

from tester import Tester


class Solution:
    def minimumLines(self, s: List[List[int]]) -> int:
        if len(s) < 3:
            return len(s) - 1
        s.sort()
        count = 1
        x1, y1 = s[0]
        x2, y2 = s[1]
        a = y2 - y1
        b = x1 - x2
        c = -a * x2 - b * y2

        for (x1, y1), (x2, y2) in zip(s[1:], s[2:]):
            if a * x2 + b * y2 + c:
                a = y2 - y1
                b = x1 - x2
                c = -a * x2 - b * y2
                count += 1
        return count


t = Tester(Solution())

t.test(
    29,
    [
        [72, 98],
        [62, 27],
        [32, 7],
        [71, 4],
        [25, 19],
        [91, 30],
        [52, 73],
        [10, 9],
        [99, 71],
        [47, 22],
        [19, 30],
        [80, 63],
        [18, 15],
        [48, 17],
        [77, 16],
        [46, 27],
        [66, 87],
        [55, 84],
        [65, 38],
        [30, 9],
        [50, 42],
        [100, 60],
        [75, 73],
        [98, 53],
        [22, 80],
        [41, 61],
        [37, 47],
        [95, 8],
        [51, 81],
        [78, 79],
        [57, 95],
    ],
)
t.test(3, [[1, 7], [2, 6], [3, 5], [4, 4], [5, 4], [6, 3], [7, 2], [8, 1]])
t.test(1, [[1, 2], [3, 3], [5, 4]])
t.test(1, [[3, 4], [1, 2], [7, 8], [2, 3]])

t.report()
