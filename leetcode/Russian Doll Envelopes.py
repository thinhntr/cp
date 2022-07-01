# https://leetcode.com/problems/russian-doll-envelopes/
from bisect import bisect_left
from typing import List

from tester import Tester


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        something = 10
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = []
        for _, h in envelopes:
            left = bisect_left(dp, h)
            if left == len(dp):
                dp.append(h)
            else:
                dp[left] = h
        return len(dp)
        

t = Tester(Solution())

t.test(3, [[5,4],[6,4],[6,7],[2,3]])
t.test(1, [[1,1],[1,1],[1,1]])

t.report()
