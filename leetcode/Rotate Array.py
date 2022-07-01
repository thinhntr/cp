# https://leetcode.com/problems/rotate-array/

from typing import List


class Solution:
    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(k):
            for i in range(n-1, 0, -1):
                j = i - 1
                nums[i], nums[j] = nums[j], nums[i]
        return nums

    def rotate2(self, nums: List[int], k: int) -> None:
        n = len(nums)
        tmp = [_ for _ in nums]
        for i in range(n):
            nums[(i + k) % n] = tmp[i]
        print(nums)
        return nums

tests = [
    ({'nums': [1, 2, 3, 4, 5, 6, 7], 'k': 3}, [5, 6, 7, 1, 2, 3, 4]),
    ({'nums': [-1, -100, 3, 99], 'k': 2}, [3, 99, -1, -100])
]
solution = Solution()


def check(solution, params, output):
    nums_id = id(params['nums'])
    result = solution.rotate(**params)
    return result == output and nums_id == id(result)


for i, (params, output) in enumerate(tests):
    print(i, check(solution, params, output))


# 1 2 3 4 5 6 7
# 7 1 2 3 4 5 6
# 6 7 1 2 3 4 5
# 5 6 7 1 2 3 4
