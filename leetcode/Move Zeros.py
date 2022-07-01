# https://leetcode.com/problems/move-zeroes 
from typing import List
from collections import deque

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = [_ for _ in nums]
        n = len(nums)
        k = 0
        for i in range(n):
            if nums[i] != 0:
                nums[k] = tmp[i]
                k += 1
        for k in range(k, n):
            nums[k] == 0
        return nums  # remove later


tests = [
    ({'nums': [0,1,0,3,12], 'k': 3}, [1,3,12,0,0]),
    ({'nums': [0], 'k': 2}, [0])
]
solution = Solution()


def check(solution, params, output):
    nums_id = id(params['nums'])
    result = solution.rotate(**params)
    return result == output and nums_id == id(result)


for i, (params, output) in enumerate(tests):
    print(i, check(solution, params, output))

