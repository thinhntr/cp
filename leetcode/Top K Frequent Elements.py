# https://leetcode.com/problems/top-k-frequent-elements/
from collections import Counter
from typing import List
from tester import Tester


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        for val, freq in Counter(nums).items():
            buckets[freq].append(val)
        res = []
        for bucket in buckets[::-1]:
            if bucket:
                res.extend(bucket)
            if len(res) == k:
                break
        return res


t = Tester(Solution())

t.test(
    [3, 7, 10], 
    [5, -3, 9, 1, 7, 7, 9, 10, 2, 2, 10, 10, 3, -1, 3, 7, -9, -1, 3, 3], 
    3
)
t.test([-1, 2], [4, 1, -1, 2, -1, 2, 3], 2)
t.test([1, 2], [1, 1, 1, 2, 2, 3], 2)
t.test([1, 2], [3, 2, 1, 2, 1, 1], 2)
t.test([1, 2, 3], [3, 2, 1, 2, 1, 1], 3)
t.test([1], [1], 1)

t.report()
