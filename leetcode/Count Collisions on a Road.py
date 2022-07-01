# https://leetcode.com/contest/weekly-contest-285/problems/count-collisions-on-a-road/
from typing import List
from tester import Tester


class Solution:
    def countCollisions(self, d: str) -> int:
        for i in range(len(d)):
            if d[i] != "L":
                break
        d = d[i:]
        count = 0
        tmp = 0
        for l, r in zip(d, d[1:]):
            if r == "S" and l == "R":
                count += 1 + tmp
                tmp = 0
            elif r == "L":
                count += (2 if l == "R" else 1) + tmp
                tmp = 0
            else:
                if l == "R":
                    tmp += 1

        return count


t = Tester(Solution())

t.test(3, "RLL")
t.test(5, "RLRSLL")
t.test(0, "LLRR")
t.test(3, "RRL")
t.test(20, "SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR")

t.report()
