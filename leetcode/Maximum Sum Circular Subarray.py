# https://leetcode.com/problems/maximum-sum-circular-subarray/
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        cur_min = glo_min = 0
        cur_max, glo_max = 0, nums[0]

        for num in nums:
            total += num

            cur_min = min(cur_min + num, 0)
            glo_min = min(cur_min,  glo_min)

            cur_max = max(cur_max + num, num)
            glo_max = max(cur_max, glo_max)

        if total != glo_min:
            return max(glo_max, total - glo_min)
        return glo_max


solution = Solution()


def check(inp, out):
    result = solution.maxSubarraySumCircular(inp)
    assert out == result


check([1, -2, 3, -2], 3)
check([1], 1)
check([5, -3, 5], 10)
check([3, -1, 2, -1], 4)
check([3, -2, 2, -3], 3)
check([3, -2, 2, -1], 4)
check([3, 2, -2, 1, 2], 8)
check([3, 2, 1, 4], 10)
check([-2, -3, -1], -1)
check([2, 3, 4, -2, -3, 5, 6, -1, -1, 2], 20)
