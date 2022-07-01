#
from typing import List
from tester import Tester


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        length = 1
        for num in nums:
            if num > nums[length - 1]:
                nums[length] = num
                length += 1
                continue

            start = 0
            end = length
            while start < end:
                m = (start + end) // 2
                if nums[m] < num:
                    start = m + 1
                else:
                    end = m

            nums[end] = num
        return length


t = Tester(Solution())

t.test(5, [10, 9, 2, 5, 3, 11, 12, 7, 10, 11])
t.test(4, [10, 9, 2, 5, 3, 7, 101, 18])
t.test(4, [0, 1, 0, 3, 2, 3])
t.test(1, [7, 7, 7, 7, 7, 7, 7])

t.report()
