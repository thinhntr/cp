# https://leetcode.com/problems/squares-of-a-sorted-array/

from typing import List
from collections import deque

from tester import Tester


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        stack = deque()
        result = deque()
        for num in nums:
            squared = num**2
            if num < 0:
                stack.append(squared)
            else:
                while stack and stack[-1] <= squared:
                    result.append(stack.pop())
                result.append(squared)
        while stack:
            result.append(stack.pop())
        return list(result)

    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        stack = []
        for num in nums:
            sqr = num**2
            if not stack or stack[-1] >= sqr:
                stack.append(sqr)
                continue
            while stack and stack[-1] < sqr:
                ans.append(stack.pop())
            stack.append(sqr)
        ans.extend(stack[::-1])
        return ans


t = Tester(Solution())

t.test([9, 16, 16], [-4, -4, -3])
t.test([0, 1, 9, 16, 100], [-4, -1, 0, 3, 10])
t.test([4, 9, 9, 49, 121], [-7, -3, 2, 3, 11])

t.report()
