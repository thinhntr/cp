# https://leetcode.com/problems/find-the-duplicate-number/
from typing import List
from tester import Tester


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            fast = nums[fast]
            fast = nums[fast]
            slow = nums[slow]
            if fast == slow:
                slow = nums[0]
                break
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return fast

t = Tester(Solution())

t.test(2, [1, 3, 4, 2, 2])
t.test(3, [3, 1, 3, 4, 2])
t.test(1, [1, 1])
t.test(1, [1, 2, 1])
t.test(3, [1, 2, 3, 3])
t.test(2, [2, 2, 2, 2, 2])
t.test(2, [2, 2, 1, 2, 3])

t.report()
