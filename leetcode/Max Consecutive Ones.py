# https://leetcode.com/problems/max-consecutive-ones/
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return len(max(''.join(map(str, nums)).split('0')))


solution = Solution()


def check(input, expected):
    output = solution.findMaxConsecutiveOnes(input)
    assert output == expected


check([1,1,0,1,1,1], 3)
check([1,0,1,1,0,1], 2)
check([1, 1, 1], 3)
check([1, 1], 2)
check([0, 0, 0], 0)