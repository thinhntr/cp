# None
import random
from random import shuffle
from typing import List


class Solution:
    def mini_median(self, nums):
        nums = sorted(nums)
        n = len(nums)
        mid = n // 2
        return nums[mid] if n & 1 else (nums[mid] + nums[mid - 1]) / 2

    def mom(self, subarrays):
        mom = [self.mini_median(subarray) for subarray in subarrays]
        return self.mini_median(mom)

    def partition(self, nums, l, r, pivot_idx):
        pivot_val = nums[pivot_idx]
        nums[r], nums[pivot_idx] = pivot_val, nums[r]
        store_idx = l
        for i in range(l, r):
            if nums[i] < pivot_val:
                nums[i], nums[store_idx] = nums[store_idx], nums[i]
                store_idx += 1
        nums[store_idx], nums[r] = nums[r], nums[store_idx], nums[r]

    def findMedian(self, nums: List[int]) -> float:
        n = len(nums)
        something = self.mom([nums[i:(i+5)] for i in range(0, n, 5)])
        print(something)


solution = Solution()


def check(input, expected):
    output = solution.findMedian(input)
    assert output == expected


random.seed(5)

a = [1, 2, 3, 4, 5, 6, 7]
b = [1, 2, 3, 4, 5, 6]

shuffle(a)
shuffle(b)

check(a, 4.)
check(b, (3 + 4) / 2)
