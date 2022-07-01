# https://leetcode.com/problems/sliding-window-maximum/
from typing import List

from collections import deque

class MaxQueue:
    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()

    @property
    def max(self):
        if not self.s1 or not self.s2:
            return self.s2[-1][1] if not self.s1 else self.s1[-1][1]
        else:
            return max(self.s1[-1][1], self.s2[-1][1])

    def append(self, value):
        maximum = value if not self.s1 else max(value, self.s1[-1][1])
        self.s1.append((value, maximum))

    def popleft(self):
        if not self.s2:
            while self.s1:
                element = self.s1[-1][0]
                self.s1.pop()
                maximum = element if not self.s2 else max(element, self.s2[-1][1])
                self.s2.append((element, maximum))
        remove_element = self.s2[-1][0]
        self.s2.pop()
        return remove_element


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_q = MaxQueue()
        result = []

        for num in nums[:k]:
            max_q.append(num)

        result.append(max_q.max)
        max_q.popleft()

        for num in nums[k:]:
            max_q.append(num)
            result.append(max_q.max)
            max_q.popleft()

        return result


solution = Solution()


def check(input, expected):
    output = solution.maxSlidingWindow(*input)
    assert output == expected


check([[1, 3, -1, -3, 5, 3, 6, 7], 3], [3, 3, 5, 5, 6, 7])
check([[1], 1], [1])
check([[1, -1], 1], [1, -1])
check([[9, 11], 2], [11])
check([[4, -2], 2], [4])

# [1, 3, -1, -3, 5, 3, 6, 7]
# [1, 3, -1, -3, 5, 3, 6, 7]
# [1, 3,  3,  3, 5, 5, 6, 7]
