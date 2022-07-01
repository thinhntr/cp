# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
from collections import Counter
from typing import List

from icecream import ic

from tester import Tester


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        top_cnt = Counter()
        bot_cnt = Counter()
        double = Counter()
        for top, bot in zip(tops, bottoms):
            top_cnt[top] += 1
            bot_cnt[bot] += 1
            if bot == top:
                double[top] += 1

        n = len(tops)
        top = tops[-1]
        bot = bottoms[-1]
        min_rotation = n

        if top_cnt[top] + bot_cnt[top] - double[top] == n:
            min_rotation = min(top_cnt[top], bot_cnt[top]) - double[top]

        if top_cnt[bot] + bot_cnt[bot] - double[bot] == n:
            min_rotation = min(top_cnt[bot], bot_cnt[bot]) - double[bot]

        return -1 if min_rotation == n else min_rotation


t = Tester(Solution())

t.test(2, [2, 1, 1, 1, 2, 2, 2, 1, 1, 2], 
          [1, 1, 2, 1, 1, 1, 1, 2, 1, 1])
t.test(0, [1, 1, 1, 1], [1, 1, 1, 1])
t.test(2, [2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2])
t.test(-1, [3, 5, 1, 2, 3], [3, 6, 3, 3, 4])
t.test(-1, [2, 3, 2, 1, 1, 1, 2, 2], [2, 1, 2, 1, 1, 3, 1, 1])
# [3,1,2,2]
# [1,3,1,1]
t.report()
