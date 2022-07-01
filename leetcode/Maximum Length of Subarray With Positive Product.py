# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/
from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        nums.append(0)
        cur_range = [0, 0]
        max_range = [0, 0]
        count_neg = 0
        first_neg_idx = last_neg_idx = -1

        for i in range(len(nums)):
            if not nums[i]:
                if count_neg & 1:
                    # split cur_range if it has an odd # of negative
                    a = cur_range[0]
                    b = last_neg_idx
                    c = first_neg_idx + 1
                    d = cur_range[1]
                    if b - a > d - c:
                        cur_range[1] = b
                    else:
                        cur_range[0] = c
                a = cur_range[0]
                b = cur_range[1]
                c = max_range[0]
                d = max_range[1]
                if b - a > d - c:
                    max_range[0] = a
                    max_range[1] = b

                count_neg = 0
                first_neg_idx = last_neg_idx = -1
                cur_range[0] = i + 1
            elif nums[i] < 0:
                count_neg += 1
                if first_neg_idx < 0:
                    first_neg_idx = i
                last_neg_idx = i

            cur_range[1] = i + 1
        return max_range[1] - max_range[0]


solution = Solution()


def check(inp, expected):
    output = solution.getMaxLen(inp)
    assert expected == output


check([-17, -9, 17, -3, -5, -13, 2, 6, 0], 7)
check([1, -2, -3, 4], 4)
check([0, 1, -2, -3, -4], 3)
check([-1, -2, -3, 0, 1], 2)
check([-1, 2], 1)
check([1, 2, 3, 5, -6, 4, 0, 10], 4)
check([1, 2, -2, -3, -4, -7, -8, 9, 4, 5], 7)
check([1, 2, -2, -3, 0, -7, -8, 9, 4, 5], 5)
