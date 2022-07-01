# https://leetcode.com/problems/partition-labels/
from typing import List
from tester import Tester


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end_idxs = {}
        for i, c in enumerate(s):
            end_idxs[c] = i

        l = m = 0
        r = end_idxs[s[0]]
        partitions = []
        while r < len(s):
            r = max(r, end_idxs[s[m]])
            if m == r:
                partitions.append(r - l + 1)
                l = r + 1
                r = end_idxs[s[l]] if l < len(s) else l
            m += 1
        return partitions


t = Tester(Solution())

t.test([1], "a")
t.test([10], "eccbbbbdec")
t.test([1, 1, 1, 1, 3, 2], "abcdegeff")
t.test([9, 7, 8], "ababcbacadefegdehijhklij")

t.report()
