# https://leetcode.com/problems/3sum/
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        result = []
        for i, num in enumerate(nums[:-2]):
            if i and (i <= 0 or nums[i] == nums[i-1]):
                continue
            l = i + 1
            r = n - 1
            total = -num
            while l < r:
                if nums[l] + nums[r] == total:
                    result.append([num, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]: 
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < total:
                    while l < r and nums[l] == nums[l + 1]: 
                        l += 1
                    l += 1
                else:
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1
        return result



solution = Solution()


def check(input, expected):
    output = solution.threeSum(input)
    assert output == expected


check([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]])
check([], [])
check([0], [])
