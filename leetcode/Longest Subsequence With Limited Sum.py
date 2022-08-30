# https://leetcode.com/problems/longest-subsequence-with-limited-sum/
import heapq
from typing import List

from tester import Tester


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(queries)
        ans = [0] * n
        nums = [-x for x in nums]
        total = sum(nums)
        heapq.heapify(nums)
        for i in range(n):
            tmp_nums = nums[:]
            tmp_total = total
            while tmp_nums and -tmp_total > queries[i]:
                tmp_total -= heapq.heappop(tmp_nums)
            ans[i] = len(tmp_nums)
        return ans


t = Tester(Solution())
t.test([2, 3, 4], [4, 5, 2, 1], [3, 10, 21])
t.test([0], [2, 3, 4, 5], [1])
t.report()
