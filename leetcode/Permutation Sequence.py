# https://leetcode.com/problems/permutation-sequence/
from itertools import accumulate
import operator
from tester import Tester

factorials = list(accumulate(range(1, 9), operator.mul))


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        nums = list(range(1, n + 1))
        result = []
        for i in reversed(range(n - 1)):
            idx = k // factorials[i]
            k = k % factorials[i]
            result.append(str(nums.pop(idx)))
        result.append(str(nums[0]))

        return "".join(result)


t = Tester(Solution())

t.test("123", 3, 1)
t.test("132", 3, 2)
t.test("213", 3, 3)
t.test("231", 3, 4)
t.test("312", 3, 5)
t.test("321", 3, 6)
t.test("1234", 4, 1)
t.test("1243", 4, 2)
t.test("2134", 4, 7)
t.test("2314", 4, 9)
t.test("54321", 5, 120)

t.report()
