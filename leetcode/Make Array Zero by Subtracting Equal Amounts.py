# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/
from typing import List

from tester import Tester


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        step = 0
        res = float("inf")
        for num in nums:
            if num:
                res = min(res, num)
        m = res if res != float("inf") else 0
        while m:
            step += 1
            tmp = float("inf")
            for i in range(len(nums)):
                if nums[i]:
                    nums[i] -= m
                if nums[i]:
                    tmp = min(nums[i], tmp)
            m = tmp if tmp != float("inf") else 0
        return step


t = Tester(Solution())

t.test(3, [1, 5, 0, 3, 5])

t.report()
