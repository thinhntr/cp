# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/
from functools import lru_cache
from typing import List

from tester import Tester


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        @lru_cache
        def digit_sum(num):
            total = 0
            while num:
                total += num % 10
                num //= 10
            return total

        mapping = {}
        max_sum = -1
        for num in nums:
            ds = digit_sum(num)
            if ds in mapping:
                total, prev = mapping[ds]
                new_total = total + num - prev
                if new_total > total:
                    mapping[ds] = [new_total, min(num, total - prev)]
                max_sum = max(max_sum, mapping[ds][0])
            else:
                mapping[ds] = [num, 0]
        return max_sum


t = Tester(Solution())

t.test(
    973,
    [
        229,
        398,
        269,
        317,
        420,
        464,
        491,
        218,
        439,
        153,
        482,
        169,
        411,
        93,
        147,
        50,
        347,
        210,
        251,
        366,
        401,
    ],
)
t.test(54, [18, 43, 36, 13, 7])
t.test(-1, [10, 12, 19, 14])

t.report()


def digit_sum(num):
    total = 0
    while num:
        total += num % 10
        num //= 10
    return total


print(digit_sum(5))
