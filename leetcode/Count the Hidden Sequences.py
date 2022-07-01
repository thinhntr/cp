# https://leetcode.com/problems/count-the-hidden-sequences/
from typing import List
from tester import Tester


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_lower = max_lower = cur_lower = lower
        min_upper = max_upper = cur_upper = upper

        for diff in differences:
            cur_lower = diff + cur_lower
            min_lower = min(min_lower, cur_lower)
            max_lower = max(max_lower, cur_lower)

            cur_upper = diff + cur_upper
            min_upper = min(min_upper, cur_upper)
            max_upper = max(max_upper, cur_upper)


        if min_lower < lower:
            amount = lower - min_lower 
            min_lower += amount
            max_lower += amount

        if max_lower > upper:
            return 0

        if upper < max_upper:
            amount = max_upper - upper 
            max_upper -= amount
            min_upper -= amount

        if min_upper < lower:
            return 0


        return max_upper - max_lower + 1


t = Tester(Solution())

t.test(2, [1, -3, 4], lower=1, upper=6)
t.test(4, [3, -4, 5, 1, -2], lower=-4, upper=5)
t.test(0, [4, -7, 2], lower=3, upper=6)

t.report()
