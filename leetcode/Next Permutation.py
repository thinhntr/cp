# https://leetcode.com/problems/next-permutation/
from typing import List
from tester import Tester


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # 1. Find the longest non-increasing suffix
        for i in reversed(range(n)):
            if i and nums[i - 1] < nums[i]:
                break

        # 2. Identify the pivot
        pivot = i - 1

        # 3. Swap the pivot with the smallest element that is greater than it
        if pivot >= 0:
            for j in reversed(range(i, n)):
                if nums[j] > nums[pivot]:
                    break
            nums[j], nums[pivot] = nums[pivot], nums[j]

        # 4. Reverse the suffix
        nums[i:] = reversed(nums[i:])

        return nums


t = Tester(Solution())

t.test([2, 1, 3], [1, 3, 2])
t.test([1, 2, 3], [3, 2, 1])
t.test([1, 5, 1], [1, 1, 5])
t.test([5, 1, 1], [1, 5, 1])
t.test([3, 7, 5, 6], [3, 6, 7, 5])
t.test([5, 1, 2, 3, 4], [4, 5, 3, 2, 1])

t.report()
