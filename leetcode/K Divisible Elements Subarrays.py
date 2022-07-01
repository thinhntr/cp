# https://leetcode.com/contest/weekly-contest-291/problems/k-divisible-elements-subarrays/
from typing import List

from tester import Tester


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        combs = set()
        n = len(nums)
        for i in range(n):
            combs.add((nums[i],))
            count = nums[i] % p == 0
            for j in range(i + 1, n):
                count += nums[j] % p == 0
                if count > k:
                    break
                combs.add(tuple(nums[i : j + 1]))
        return len(combs)


t = Tester(Solution())

t.test(11, [2, 3, 3, 2, 2], 2, 2)
t.test(10, [1, 2, 3, 4], 4, 1)
t.test(14, [10, 2, 17, 7, 20], 1, 10)

t.report()
