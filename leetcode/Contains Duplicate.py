# https://leetcode.com/problems/contains-duplicate/
from typing import List
from collections import Counter


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return any(c > 1 for c in Counter(nums).values())


solution = Solution()


def check(input, expected):
    output = solution.containsDuplicate(input)
    assert output == expected


check([1, 2, 3, 1], True)
check([1, 2, 3, 4], False)
check([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True)
