# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
from typing import List
from tester import Tester


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return True
            if nums[l] == nums[m] == nums[r]:
                l += 1
                r -= 1
            elif nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return False


t = Tester(Solution())

t.test(True, [1, 13, 1, 1, 1, 1], 13)
t.test(True, [1, 1, 1, 1, 1, 1, 1, 1, 1, 13, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 13)
t.test(True, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], 2)
t.test(True, [1, 0, 1, 1, 1], 0)
t.test(False, [2, 6, 0, 0, 1, 2], 3)
t.test(True, [2, 2, 5, 6, 0, 0, 1], 0)
t.test(True, [2, 5, 6, 0, 0, 1, 2], 0)
t.test(False, [2, 5, 6, 0, 0, 1, 2], 3)
t.test(True, [5, 5, 5, 5, 5, 5, 5], 5)
t.test(False, [5, 5, 5, 5, 5, 5, 5], 6)

t.report()
