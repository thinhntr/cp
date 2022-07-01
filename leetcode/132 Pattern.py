# https://leetcode.com/problems/132-pattern/
from typing import List

from tester import Tester


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        left_less_idx = list(range(n))
        ptr = 0
        for i in range(1, n):
            if nums[ptr] >= nums[i]:
                ptr = i
            else:
                left_less_idx[i] = ptr

        right_greater_idx = list(range(n))
        stack = [n - 1]
        for i in reversed(range(1, n - 1)):
            while stack and nums[i] > nums[stack[-1]]:
                top = stack.pop()
                right_greater_idx[top] = i
            stack.append(i)
        for i in range(n):
            lli = left_less_idx[i]
            rgi = right_greater_idx[i]
            if lli < rgi < i:
                return True
        return False


t = Tester(Solution())

t.test(True, [3, 5, 0, 3, 4])
t.test(False, [1, 2, 3, 4])
t.test(True, [3, 1, 4, 2])
t.test(True, [-1, 3, 2, 0])
t.test(False, [7, 5, 4, 1, 3])

t.report()
