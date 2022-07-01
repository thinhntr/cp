# https://leetcode.com/problems/boats-to-save-people/
from typing import List
from tester import Tester


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        l, r = 0, len(people) - 1
        while l <= r:
            r -= l != r and people[l] + people[r] <= limit
            l += 1
        return l


t = Tester(Solution())

t.test(1, [1, 2], 3)
t.test(2, [2, 4], 5)
t.test(3, [1, 1, 1, 3], 3)
t.test(3, [3, 2, 2, 1], 3)
t.test(4, [3, 5, 3, 4], 5)
t.test(2, [1, 1, 2, 1], 3)
t.test(3, [1, 1, 2, 1, 1], 3)
t.test(2, [2, 2, 1, 1], 3)
t.test(
    11, [2, 49, 10, 7, 11, 41, 47, 2, 22, 6, 13, 12, 33, 18, 10, 26, 2, 6, 50, 10], 50
)
t.report()
