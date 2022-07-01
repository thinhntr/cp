# https://leetcode.com/problems/shuffle-an-array/

import random
from operator import itemgetter
from typing import List

from icecream import ic


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.indices = list(range(len(nums)))

    @property
    def size(self):
        return len(self.nums)

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        weights = [random.random() for _ in range(self.size)]
        wi = zip(weights, self.indices)
        wi = sorted(wi, key=itemgetter(0))
        return [self.nums[p[1]] for p in wi]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
random.seed(5)
obj = Solution([1, 2, 3, 4, 5, 6])
ic(obj.shuffle())
ic(obj.reset())
ic(obj.shuffle())
ic(obj.shuffle())
ic(obj.reset())
