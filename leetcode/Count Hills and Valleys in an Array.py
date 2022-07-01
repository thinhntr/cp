# https://leetcode.com/contest/weekly-contest-285/problems/count-hills-and-valleys-in-an-array/
from typing import List
from tester import Tester


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        m = 1
        count = 0
        while m < n - 1:
            if nums[l] == nums[m]:
                l += 1
                m += 1
                continue

            r = m + 1
            while r < n and nums[r] == nums[m]:
                r += 1
            if r == n:
                break

            if nums[l] < nums[m] and nums[m] > nums[r]:
                count += 1
            elif nums[l] > nums[m] and nums[m] < nums[r]:
                count += 1
            l += 1
            m += 1

        return count


t = Tester(Solution())

t.test(0, [6, 6, 5, 5, 4, 1])
t.test(0, [1, 2, 3, 4])
t.test(1, [1, 2, 3, 4, 3])
t.test(3, [2, 4, 1, 1, 6, 5])

t.report()
