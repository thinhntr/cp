# https://leetcode.com/problems/delete-and-earn/
from collections import Counter
from tester import Tester
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        mmax = [0] * 10_001

        for num in nums:
            mmax[num] += num

        mmax[2] += mmax[0]
        for i in range(3, 10_001):
            mmax[i] += max(mmax[i - 2], mmax[i - 3])

        return max(mmax)

    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for num in counter:
            counter[num] *= num

        numset = sorted(counter.keys())
        for i in range(len(numset)):
            i1 = i - 1 if i > 0 and numset[i - 1] + 1 != numset[i] else i - 2
            i0 = i1 - 1
            prev1 = counter[numset[i1]] if i1 >= 0 else 0
            prev0 = counter[numset[i0]] if i0 >= 0 else 0
            counter[numset[i]] += max(prev0, prev1)

        return max(counter.values())


t = Tester(Solution())

t.test(18, [1, 1, 1, 2, 4, 5, 5, 5, 6])
t.test(6, [3, 4, 2])
t.test(9, [2, 2, 3, 3, 3, 4])
t.test(15, [3, 2, 3, 2, 3, 4, 5, 6])

t.report()
