# https://leetcode.com/problems/permutations/
from typing import List

from itertools import permutations
# https://github.com/python/cpython/blob/main/Modules/itertoolsmodule.c

class Solution:
    def blabla(self, current, indicies):
        if not indicies:
            self.result.append(current)
            return

        current.append(None)
        for index in indicies:
            current[-1] = self.nums[index]
            self.blabla(current[:], indicies - {index})

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.result = []
        n = len(nums)
        indices = set(range(n))
        self.blabla([], indices)
        return self.result
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))


solution = Solution()


def to_set(ll):
    return set(map(tuple, ll))


def check(iterable, output):
    result = solution.permute(iterable)
    assert len(result) == len(output) and to_set(result) == to_set(output)


check([1, 2, 3], [[1, 2, 3],
                  [1, 3, 2],
                  [2, 1, 3],
                  [2, 3, 1],
                  [3, 1, 2],
                  [3, 2, 1]])

check([0, 1], [[1, 0], [0, 1]])
check([1], [[1]])
check([], [[]])
