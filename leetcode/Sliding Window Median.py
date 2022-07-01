# https://leetcode.com/problems/sliding-window-median/
from bisect import insort
from typing import List
from tester import Tester


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = sorted(nums[:k])
        meds = []
        for l, r in zip(nums, nums[k:] + [0]):
            meds.append((window[k // 2] + window[~(k // 2)]) / 2)
            window.remove(l)
            insort(window, r)
        return meds


t = Tester(Solution())

t.test(
    [1.00000, -1.00000, -1.00000, 3.00000, 5.00000, 6.00000],
    nums=[1, 3, -1, -3, 5, 3, 6, 7],
    k=3,
)
t.test(
    [2.0, 3.0, 3.0, 3.0, 2.0, 3.0, 2.0],
    nums=[1, 2, 3, 4, 2, 3, 1, 4, 2],
    k=3,
)

t.report()
