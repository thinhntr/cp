# https://leetcode.com/problems/last-stone-weight/
from operator import neg
from heapq import heapify, heappop, heappush
from typing import List

from tester import Tester


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(neg, stones))
        heapify(stones)
        while len(stones) > 1:
            x = heappop(stones)
            y = heappop(stones)
            if y - x:
                heappush(stones, x - y)
        return -stones[0] if stones else 0


t = Tester(Solution())

t.test(1, [2, 7, 4, 1, 8, 1])
t.test(1, [1])

t.report()
