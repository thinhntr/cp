# https://leetcode.com/contest/weekly-contest-295/problems/steps-to-make-array-non-decreasing/
from typing import List

from tester import Tester


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        stack = []
        res = 0
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                dp[i] = max(dp[i] + 1, dp[stack.pop()])
                res = max(res, dp[i])
            stack.append(i)
        return res


t = Tester(Solution())

t.test(3, [7, 14, 4, 14, 13, 2, 6, 13])
t.test(1, [7, 11, 1])
t.test(6, [10, 1, 2, 3, 4, 5, 6, 1, 2, 3])
t.test(7, [10, 1, 2, 3, 1, 2, 3, 4, 5, 6])
t.test(3, [5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11])
t.test(2, [6, 6, 2, 7, 1, 6, 10, 5, 3, 7])
t.test(0, [4, 5, 7, 7, 13])
t.test(3, [6, 6, 2, 7, 1, 6, 10, 3, 5, 7])


t.report()

# 7, 14, 4, 14, 13, 2, 6, 13
#        ^       ^

# 10, 1, 2, 3, 4, 5, 6, 1, 2, 3
#     ^                 ^

# 10, 1, 2, 3, 1, 2, 3, 4, 5, 6
#     ^        ^

# 5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11
#    ^  ^  ^     ^  ^      ^  ^

# 6, 6, 2, 7, 1, 6, 10, 5, 3, 7
#       ^     ^  ^      ^  ^  ^

# 4, 5, 7, 7, 13
#


# 6, 6, 2, 7, 1, 6, 10, 3, 5, 7
#       ^     ^  ^      ^  ^  ^
