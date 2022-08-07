# https://leetcode.com/problems/count-number-of-bad-pairs/
from collections import Counter
from typing import List

from tester import Tester


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n - 1) // 2
        counter = Counter([-nums[0]])
        for i, num in enumerate(nums[1:], 1):
            total -= counter[i - num]
            counter[i - num] += 1
        return total


t = Tester(Solution())

t.test(0, [1, 2, 3, 4, 5])
t.test(5, [4, 1, 3, 3])

t.report()
