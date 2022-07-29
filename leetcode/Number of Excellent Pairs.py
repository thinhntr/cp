# https://leetcode.com/problems/number-of-excellent-pairs/
from collections import Counter
from typing import List

from tester import Tester


class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        counter = Counter(map(int.bit_count, set(nums)))
        total = 0
        for bit1 in counter:
            for bit2 in counter:
                if bit1 + bit2 >= k:
                    total += counter[bit1]*counter[bit2]
        return total



t = Tester(Solution())

t.test(0, [5, 1, 1], 10)
t.test(5, [1, 2, 3, 1], 3)

t.report()
