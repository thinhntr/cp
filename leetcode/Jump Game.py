# https://leetcode.com/problems/jump-game/
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dest = len(nums) - 1
        for i in reversed(range(dest)):
            if i + nums[i] >= dest:
                dest = i
        return dest == 0
        


solution = Solution()

assert solution.canJump([2, 3, 1, 1, 4]) == True
assert solution.canJump([3, 2, 1, 0, 4]) == False
assert solution.canJump([5, 0]) == True
assert solution.canJump([5]) == True
assert solution.canJump([0]) == True
assert solution.canJump([1]) == True
