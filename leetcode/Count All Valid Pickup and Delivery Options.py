# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/
import math
from tester import Tester


class Solution:
    def countOrders(self, n: int) -> int:
        return math.factorial(2 * n) >> n % (10**9 + 7)


t = Tester(Solution())

t.test(1, 1)
t.test(6, 2)
t.test(90, 3)

t.report()
