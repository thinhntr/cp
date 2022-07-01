# https://leetcode.com/problems/house-robber/
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        logits = nums[:]

        logits[n - 2 - 1] += logits[n - 1]
        for node in reversed(range(n - 2 - 1)):
            parent1 = node + 2
            parent2 = node + 3

            x_pre = max(logits[parent1], logits[parent2])
            logits[node] += x_pre

        return max(logits[0], logits[1])


solution = Solution()

assert solution.rob([1, 2, 3, 1]) == 4
assert solution.rob([2, 7, 9, 3, 1]) == 12
assert solution.rob([2, 1, 1, 2]) == 4
assert solution.rob([2, 0, 0, 0, 0, 2]) == 4
