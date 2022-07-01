# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cpm_pos = dict()
        for i, num in enumerate(nums):
            if num in cpm_pos:
                return i, cpm_pos[num]
            complement = target - num
            cpm_pos[complement] = i


solution = Solution()


def check(input, expected):
    output = sorted(solution.twoSum(input[0], input[1]))
    assert output == expected


check([[-1, -2, -3, -4, -5], -8], [2, 4])
check([[2, 7, 11, 15], 9], [0, 1])
check([[-3, 4, 3, 90], 0], [0, 2])
check([[0, 4, 3, 0], 0], [0, 3])
check([[3, 2, 4], 6], [1, 2])
check([[3, 3], 6], [0, 1])
