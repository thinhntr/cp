# https://leetcode.com/problems/arithmetic-slices/
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 3:
            return 0

        nums.append(2 * nums[-1] - nums[-2] - 1)
        diff = nums[0] - nums[1] - 1
        count_subarr = 0
        count_contig = -1
        count_slices = 0

        for i in range(n):
            c_diff = nums[i] - nums[i + 1]
            if c_diff != diff:
                count_slices += count_subarr
                diff = c_diff
                count_subarr = 0
                count_contig = -1
            else:
                count_contig += 1
                count_subarr += count_contig + 1

        return count_slices

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        count = 0
        prev_diff = nums[1] - nums[0]
        sublen = 2
        for i in range(2, n):
            diff = nums[i] - nums[i - 1]
            if prev_diff != diff:
                prev_diff = diff
                sublen = 2
            else:
                sublen += 1
            count += sublen - 2
        return count


solution = Solution()


def check(input, expected):
    output = solution.numberOfArithmeticSlices(input)
    assert output == expected


check([1, 2, 3, 4], 3)
check([1], 0)
check([1, 2, 3, 4, 5, 6], 10)
# 6=4+3+2+1
# 5=3+2+1
# 4=2+1->3
# 3=1->2
# 2=0->1
# 1=-1
