# https://leetcode.com/problems/sort-colors/
from typing import List
from tester import Tester


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        firstone = 0
        firsttwo = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[firstone] = nums[firstone], nums[i]
                firstone += 1
                firsttwo += nums[i] != 1
            if nums[i] == 1:
                nums[i], nums[firsttwo] = nums[firsttwo], nums[i]
                firsttwo += 1

        return nums


t = Tester(Solution())
t.test([0, 0, 1, 1, 2, 2], [2, 0, 2, 1, 1, 0])
t.test([0, 1, 2], [2, 0, 1])
t.test([0, 1, 2], [1, 0, 2])
t.test([2, 2, 2], [2, 2, 2])
t.test([1, 1, 2], [1, 2, 1])
t.test([0, 0, 0], [0, 0, 0])
t.test([0, 1], [0, 1])
t.test([0, 1], [1, 0])
t.test([0, 2], [2, 0])
t.test([0, 2], [0, 2])
t.test([1, 2], [1, 2])
t.test([1, 2], [2, 1])
t.report()
