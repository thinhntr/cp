# https://leetcode.com/contest/weekly-contest-287/problems/maximum-candies-allocated-to-k-children/
from typing import List
from tester import Tester


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def num_piles(size):
            count = 0
            for candy in candies:
                count += candy // size
            return count
        l, r = 1, sum(candies) // k
        res = 0
        while l <= r:
            m = (l + r) // 2
            num = num_piles(m)
            if num >= k:
                res = m
                l = m + 1
            else:
                r = m - 1
        return res
 

t = Tester(Solution())

t.test(5, [5, 8, 6], 3)
t.test(0, [2, 5], 11)

t.report()
