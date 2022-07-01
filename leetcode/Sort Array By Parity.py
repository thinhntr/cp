# https://leetcode.com/problems/sort-array-by-parity/
from typing import List

from tester import Tester


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res = nums[:]
        j = 0
        for i in range(len(res)):
            if res[i] % 2 == 0:
                res[i], res[j] = res[j], res[i]
                j += 1
        return res


t = Tester(Solution())

t.test([2, 4, 3, 1], [3, 1, 2, 4])
t.test([0], [0])

t.report()
