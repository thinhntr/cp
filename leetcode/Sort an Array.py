# https://leetcode.com/problems/sort-an-array/
from typing import List
import random
from random import randint


def swap(nums, a, b):
    nums[a], nums[b] = nums[b], nums[a]


class Solution:
    def bubble_down(self, nums, n, p):
        l = p
        c = p * 2

        if c < n and nums[c] > nums[l]:
            l = c

        if c + 1 < n and nums[c + 1] > nums[l]:
            l = c + 1

        if l != p:
            nums[l], nums[p] = nums[p], nums[l]
            self.bubble_down(nums, n, l)

    def bubble_sort(self, nums):
        n = len(nums)
        sorted_nums = nums[:]

        for i in reversed(range(n // 2 + 1)):
            self.bubble_down(sorted_nums, n, i)

        while n > 1:
            sorted_nums[0], sorted_nums[n - 1] = \
                sorted_nums[n - 1], sorted_nums[0]
            n -= 1
            self.bubble_down(sorted_nums, n, 0)

        return sorted_nums

    def partition(self, nums, l, r, pivot_idx):
        pivot_val = nums[pivot_idx]
        swap(nums, r, pivot_idx)
        store_idx = l

        for i in range(l, r):
            if nums[i] < pivot_val:
                swap(nums, i, store_idx)
                store_idx += 1

        swap(nums, store_idx, r)
        return store_idx

    def hoare_partition(self, nums, l, r):
        pivot_val = nums[l]
        i = l - 1
        j = r + 1
        while True:
            while True:
                i += 1
                if nums[i] >= pivot_val:
                    break

            while True:
                j -= 1
                if nums[j] <= pivot_val:
                    break

            if i >= j:
                return j

            swap(nums, i, j)

    def quick_sort_main(self, nums, l, r):
        if l >= r:
            return nums
        pivot_idx = self.hoare_partition(nums, l, r)
        self.quick_sort_main(nums, l, pivot_idx)
        self.quick_sort_main(nums, pivot_idx + 1, r)
        return nums

    def quick_sort(self, nums):
        sorted_nums = nums[:]
        return self.quick_sort_main(sorted_nums, 0, len(nums) - 1)

    def merge_sort_main(self, nums, l, r):
        if l >= r:
            return nums
        m = (l + r) // 2

        self.merge_sort_main(nums, l, m)
        self.merge_sort_main(nums, m + 1, r)

        i, j, k = l, m + 1, 0
        tmp = nums[l:r+1]

        while i <= m and j <= r:
            if nums[i] < nums[j]:
                tmp[k] = nums[i]
                i += 1
            else:
                tmp[k] = nums[j]
                j += 1
            k += 1

        while i <= m:
            tmp[k] = nums[i]
            k += 1
            i += 1

        while j <= r:
            tmp[k] = nums[j]
            k += 1
            j += 1
        nums[l:r+1] = tmp
        return nums

    def merge_sort(self, nums):
        sorted_nums = nums[:]
        return self.merge_sort_main(sorted_nums, 0, len(nums) - 1)

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quick_sort(nums)


solution = Solution()


def check(input, expected):
    output = solution.sortArray(input)
    assert output == expected


random.seed(5)

a = [randint(1, 100) for _ in range(randint(5, 18))]
b = [randint(1, 100) for _ in range(randint(5, 18))]
c = [randint(1, 100) for _ in range(randint(5, 18))]
d = [randint(1, 100) for _ in range(randint(5, 18))]

check(a, sorted(a))
check(b, sorted(b))
check(c, sorted(c))
check(d, sorted(d))

check([0], [0])
check([5, 2, 6], [2, 5, 6])
check([5, 2, 3, 1], [1, 2, 3, 5])
check([5, 1, 1, 2, 0, 0], [0, 0, 1, 1, 2, 5])
