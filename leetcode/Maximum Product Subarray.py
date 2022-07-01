# https://leetcode.com/problems/maximum-product-subarray/
from typing import List


class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        first_num = nums[0]
        first_num_is_neg = first_num < 0
        first_neg_prod = first_num if first_num_is_neg else 1
        first_neg_idx = 0 if first_num_is_neg else -1
        global_max = current_product = first_num

        for i in range(1, n):
            num = nums[i]

            if not current_product or not num:
                first_neg_prod = 1
                first_neg_idx = -1
                current_product = num
            else:
                current_product *= num

            if first_neg_prod == 1 and num < 0:
                first_neg_prod = current_product
                first_neg_idx = i

            neg_product = current_product

            if first_neg_idx > -1 and i != first_neg_idx:
                neg_product = current_product // first_neg_prod

            global_max = max(global_max, current_product, neg_product)
        return global_max


solution = Solution()


def check(inp, out):
    result = solution.maxProduct(inp)
    assert out == result


check([3, -1, 4], 4)
check([-2, 3, -4], 24)
check([2, 3, -2, -4], 48)
check([2, 3, -2, -4, -3], 48)
check([2, 3, -2, -4, -3, -10], 1440)
check([2, 3, -2, -4, -3, 10, 10], 1200)
check([2, 3, -2, -4, -3, -4, -2, 10, 10], 9600)
check([2, 3, -2, 4], 6)
check([-2, 0, -1], 0)
check([-2, 1, -1], 2)
check([0, 2], 2)
check([0, -2, -2, 0], 4)
check([-2], -2)
check([1], 1)
check([0], 0)
