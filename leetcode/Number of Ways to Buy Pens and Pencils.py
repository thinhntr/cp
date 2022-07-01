# https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/
from icecream import ic
from tester import Tester


class Solution:
    def waysToBuyPensPencils(self, total: int, c1: int, c2: int) -> int:
        ans = 1  # x=0 y=0
        ans += total // c2  # x = 0
        
        # 0 <= x*c1 + y*c2 <= total
        # 0 <=      x      <= (total - y*c2) // c1
        y = 0
        x = (total - y * c2) // c1
        while x >= 0:
            ans += x
            y += 1
            x = (total - y * c2) // c1
        return ans


t = Tester(Solution())

t.test(5151, 100, 1, 1)
t.test(9, 20, 10, 5)
t.test(1, 5, 10, 10)

t.report()
