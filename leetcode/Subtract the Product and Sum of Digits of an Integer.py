# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
from functools import reduce
from operator import add, mul

from tester import Tester


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = list(map(int, str(n)))
        return reduce(mul, n) - reduce(add, n)


t = Tester(Solution())

t.test(-2, 114)
t.test(15, 234)
t.test(21, 4421)

t.report()
