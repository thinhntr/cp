# https://leetcode.com/problems/validate-stack-sequences/
from typing import List
from tester import Tester


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        stack = []
        p2 = 0

        for num in pushed:
            while stack and stack[-1] == popped[p2]:
                p2 += 1
                stack.pop()
            stack.append(num)
        
        while stack and p2 < n and stack[-1] == popped[p2]:
            p2 += 1
            stack.pop()
            
        return not stack and p2 == n

t = Tester(Solution())

t.test(True, [0, 2, 1], [0, 1, 2])
t.test(True, [1, 2, 3, 4, 5], [4, 5, 3, 2, 1])
t.test(False, [1, 2, 3, 4, 5], [4, 3, 5, 1, 2])

t.report()
