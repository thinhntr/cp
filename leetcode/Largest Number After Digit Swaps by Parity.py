# https://leetcode.com/contest/weekly-contest-288/problems/largest-number-after-digit-swaps-by-parity
from typing import List
from tester import Tester


class Solution:
    def largestInteger(self, num: int) -> int:
        nums = list(map(int, str(num)))
        odd = []
        even = []
        odd_num = []
        even_num = []
        for i in range(len(nums)):
            if nums[i] % 2:
                odd.append(i)
                odd_num.append(nums[i])
            else:
                even.append(i)
                even_num.append(nums[i])
        odd_num.sort(reverse=True)
        even_num.sort(reverse=True)
        res = [0] * len(nums)
        for i, o in enumerate(odd):
            res[o] = odd_num[i]
        for i, e in enumerate(even):
            res[e]  = even_num[i]
        return int(''.join(map(str, res)))


t = Tester(Solution())

t.test(3412, 1234)
t.test(87655, 65875)

t.report()
