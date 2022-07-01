# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
from typing import List
from collections import Counter

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List:
        counter = Counter(nums)
        accum = 0
        
        if 0 in counter:
            accum = counter[0]
            counter[0] = 0

        for i in range(1, 101):
            if i in counter:
                accum, counter[i] = accum + counter[i], accum
                        
        
        return [counter[num] for num in nums]


solution = Solution()


def check(input, expected):
    output = solution.smallerNumbersThanCurrent(input)
    assert output == expected


check([8, 1, 2, 2, 3], [4, 0, 1, 1, 3])
check([6, 5, 4, 8], [2, 1, 0, 3])
check([7, 7, 7, 7], [0, 0, 0, 0])
