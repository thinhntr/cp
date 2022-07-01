# https://leetcode.com/problems/house-robber-ii/
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        nums1 = nums[:]

        if n > 3:
            nums1[2] += nums1[0]

        for i in range(3, n - 1):
            nums1[i] += max(nums1[i - 2], nums1[i - 3])

        max1 = max(nums1)
        nums2 = nums[:]

        if n > 3:
            nums2[3] += nums[1]

        for i in range(4, n):
            nums2[i] += max(nums2[i - 2], nums2[i - 3])
            
        max2 = max(nums2)

        return max(max1, max2)


tests = (
    ([2, 3, 2], 3),
    ([1, 2, 3, 1], 4),
    ([1, 2, 3], 3)
)

solution = Solution()


def check(inp, out):
    res = solution.rob(inp)
    assert res == out


for inp, out in tests:
    check(inp, out)
