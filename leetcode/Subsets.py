# https://leetcode.com/problems/subsets/

from typing import List
from itertools import chain, combinations
from collections import deque


def is_one(num, pos) -> bool:
    return (num >> pos) & 1


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return list(
            chain.from_iterable(combinations(nums, r) for r in range(len(nums) + 1))
        )

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = deque()
        n = len(nums)

        for mask in range(2**n):
            result.append(deque())
            for pos in range(n):
                if is_one(mask, pos):
                    result[-1].append(nums[pos])

        return result


print(Solution().subsets([1, 2, 3]))
