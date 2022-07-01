# https://leetcode.com/problems/kth-largest-element-in-an-array/
from typing import List
from collections import Counter
import random
from random import randint

random.seed(5)


def swap(array, a, b):
    array[a], array[b] = array[b], array[a]


class Solution:
    def partition(self, nums, l, r, pivot_idx):
        pivot_val = nums[pivot_idx]
        swap(nums, r, pivot_idx)
        tmp_r = l

        for i in range(l, r):
            if nums[i] >= pivot_val:
                swap(nums, i, tmp_r)
                tmp_r += 1

        tmp_l = tmp_r

        for i in reversed(range(l, tmp_r)):
            if nums[i] == pivot_val:
                tmp_l -= 1
                swap(nums, i, tmp_l)

        swap(nums, r, tmp_r)
        return tmp_l, tmp_r

    def kth_small_main(self, nums, l, r, k):
        # if l >= r:
        #     return nums[l]  # need to be reviewed

        pivot_l, pivot_r = self.partition(nums, l, r, randint(l, r))

        if k < pivot_l:
            # need to be reviewed
            return self.kth_small_main(nums, l, pivot_l - 1, k)
        elif pivot_r < k:
            return self.kth_small_main(nums, pivot_r + 1, r, k)

        return nums[pivot_l]

    def kth_large_dict(self, nums, k):
        counter = Counter(nums)
        min_val = -int(1e4)
        max_val = int(1e4) + 1
        kc = 0
        for i in reversed(range(min_val, max_val)):
            if i in counter:
                kc += counter[i]
                if kc >= k:
                    return i

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # return self.kth_small_main(nums, 0, len(nums) - 1, k - 1)
        return self.kth_large_dict(nums, k)


solution = Solution()


def check(input, expected):
    output = solution.findKthLargest(input[0], input[1])
    assert output == expected


check([[5], 1], 5)
check([[50, 2], 2], 2)
check([[4, 4, 4, 5], 1], 5)
check([[4, 4, 4, 5], 2], 4)
check([[4, 4, 4, 5], 3], 4)
check([[4, 4, 4, 5], 4], 4)

a = [randint(-5, 5) for _ in range(5)]
b = [randint(-100, 100) for _ in range(20)]
c = [randint(-100, 100) for _ in range(20)]
d = [randint(-100, 100) for _ in range(20)]
e = [randint(-100, 100) for _ in range(20)]
f = [randint(-100, 100) for _ in range(101)]
g = [randint(-100, 100) for _ in range(101)]
h = [randint(-100, 100) for _ in range(101)]

check([a, 3], sorted(a, reverse=True)[2])
check([b, 10], sorted(b, reverse=True)[9])
check([c, 11], sorted(c, reverse=True)[10])
check([d, 9], sorted(d, reverse=True)[8])
check([e, 12], sorted(e, reverse=True)[11])
check([f, 50], sorted(f, reverse=True)[49])
check([g, 49], sorted(g, reverse=True)[48])
check([h, 51], sorted(h, reverse=True)[50])
