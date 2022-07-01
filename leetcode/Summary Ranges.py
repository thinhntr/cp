# https://leetcode.com/problems/summary-ranges/submissions/

from tester import Tester
from collections import deque
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        nums = nums[::-1]
        result = deque()
        while nums:
            start = nums.pop()
            prev = start
            while nums and nums[-1] == prev + 1:
                prev = nums.pop()
            if start != prev:
                result.append(f"{start}->{prev}")
            else:
                result.append(str(start))
        return list(result)

t = Tester(Solution())        

t.test(["0->2","4->5","7"],[0,1,2,4,5,7])
t.test(["0","2->4","6","8->9"],[0,2,3,4,6,8,9])

t.report()