# https://leetcode.com/contest/weekly-contest-291/problems/minimum-consecutive-cards-to-pick-up/
from typing import List
# from collections import defaultdict
from tester import Tester

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        pos = {}
        min_dist = float('inf')
        for i, card in enumerate(cards):
            if card in pos:
                min_dist = min(min_dist, i - pos[card] + 1)
            pos[card] = i
        return min_dist if min_dist != float('inf') else -1

t = Tester(Solution())

t.test(4, [3,4,2,3,4,7])
t.test(-1, [1,0,5,3])
t.test(2, [3, 4, 5, 6, 7, 3, 3, 4])

t.report()