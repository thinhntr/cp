# https://leetcode.com/problems/maximum-subarray/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        glo_sum = cur_sum = nums[0]
        for num in nums[1:]:
            cur_sum = max(num, num + cur_sum)
            if cur_sum > glo_sum:
                glo_sum = cur_sum            
        return glo_sum


solution = Solution()


def check(inp, out):
    result = solution.maxSubArray(inp)
    assert out == result


check([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)
check([1], 1)
check([5, 4, -1], 9)
check([5, 4, -1, 0], 9)
check([5, 4, -1, 1], 9)
check([5, 4, -1, 2], 10)
check([5, 4, -1, -2], 9)
check([1, 1, -2, -1, 4], 4)
check([5, 4, -2, -1, 4], 10)
check([5, 4, -1, 7, 8], 23)
