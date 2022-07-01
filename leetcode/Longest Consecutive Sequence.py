# https://leetcode.com/problems/longest-consecutive-sequence/
from typing import List

from tester import Tester


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in nums:
            l = 0
            # Check if it is the start of the sequence
            if num - 1 not in num_set:
                while num + l in num_set:
                    l += 1
                longest = max(longest, l)
        return longest


t = Tester(Solution())

t.test(4, [100, 4, 200, 1, 3, 2])
t.test(9, [0, 3, 7, 2, 5, 8, 4, 6, 0, 1])

t.report()
