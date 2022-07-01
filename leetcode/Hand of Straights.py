# https://leetcode.com/problems/hand-of-straights/submissions/
from collections import Counter
from typing import List

from tester import Tester


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize:
            return False

        counter = Counter(hand)
        keys = sorted(counter.keys())
        minKeyIdx = 0
        numGroup = n // groupSize

        for i in range(numGroup):
            while minKeyIdx < len(keys) and not counter[keys[minKeyIdx]]:
                minKeyIdx += 1
            if minKeyIdx >= len(keys):
                return False

            key = keys[minKeyIdx]
            for i in range(groupSize):
                if not counter[key + i]:
                    return False
                counter[key + i] = counter[key + i] - 1
        return True


t = Tester(Solution())

t.test(True, [1, 2, 3], 3)
t.test(True, [8, 8, 9, 7, 7, 7, 6, 7, 10, 6], 2)
t.test(True, [1, 2, 3, 6, 2, 3, 4, 7, 8], 3)
t.test(False, [8, 10, 12], 3)
t.test(False, [1, 2, 3, 4, 5], 4)

t.report()
