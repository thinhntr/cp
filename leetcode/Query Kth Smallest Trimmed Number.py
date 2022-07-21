# https://leetcode.com/problems/query-kth-smallest-trimmed-number/
from typing import List

from tester import Tester


class Solution:
    def smallestTrimmedNumbers(
        self, nums: List[str], queries: List[List[int]]
    ) -> List[int]:
        res = []
        for k, trim in queries:
            result = sorted((int(num[-trim:]), idx) for idx, num in enumerate(nums))
            num = result[k - 1][1]
            res.append(num)
        return res


t = Tester(Solution())

t.test([2, 2, 1, 0], ["102", "473", "251", "814"], [[1, 1], [2, 3], [4, 2], [1, 2]])
t.test([3, 0], ["24", "37", "96", "04"], [[2, 1], [2, 2]])

t.report()
