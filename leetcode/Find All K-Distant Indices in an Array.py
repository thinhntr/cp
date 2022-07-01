# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/
from tester import Tester
from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        key_idxs = []
        for i in range(n):
            if nums[i] == key:
                key_idxs.append(i)
        key_idxs = key_idxs[::-1]

        idxs = []
        curr_key = key_idxs.pop()
        for i in range(n):
            if i - curr_key > k:
                if not key_idxs:
                    break
                curr_key = key_idxs.pop()
            
            if abs(curr_key - i) <= k:
                idxs.append(i)

        return list(idxs)


t = Tester(Solution())

t.test([1, 2, 3, 4, 5, 6], [3, 4, 9, 1, 3, 9, 5], 9, 1)
t.test([0, 1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2, 5)
t.test(list(range(5)), [2,2,2,2,2], 2, 2)

t.report()
