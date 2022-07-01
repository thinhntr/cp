# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

#
from typing import List
from tester import Tester
from operator import itemgetter


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return map(
            itemgetter(1), sorted(((sum(row), i) for i, row in enumerate(mat)))[:k]
        )


t = Tester(Solution())

t.test([0, 2], [[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]], 2)

t.test(
    [2, 0, 3],
    [
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1],
    ],
    3,
)

t.report()
