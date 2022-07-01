# https://leetcode.com/contest/weekly-contest-288/problems/maximum-product-after-k-increments/
from functools import reduce
from heapq import heapify, heappushpop
from typing import List

from tester import Tester


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapify(nums)   
        while k:
            heappushpop(nums, nums[0] + 1)
            k -= 1
        mul = lambda a, b: a * b % 1_000_000_007 
        return reduce(mul, nums)


t = Tester(Solution())

t.test(20, nums=[0, 4], k=5)
t.test(216, nums=[6, 3, 3, 2], k=2)

t.report()
