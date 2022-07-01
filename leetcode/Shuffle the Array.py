# https://leetcode.com/problems/shuffle-the-array/
from typing import List

from tester import Tester


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        pos = lambda i: i // 2 + (n if i % 2 else 0)
        return [nums[pos(i)] for i in range(2 * n)]


t = Tester(Solution())

t.test([1, 2, 1, 2], [1, 1, 2, 2], 2)
t.test([2, 3, 5, 4, 1, 7], [2, 5, 1, 3, 4, 7], 3)
t.test([1,4,2,5,3,6],[1,2,3,4,5,6],3)
t.test([1, 4, 2, 3, 3, 2, 4, 1], [1, 2, 3, 4, 4, 3, 2, 1], 4)


t.report()
