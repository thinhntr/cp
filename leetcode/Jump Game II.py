# https://leetcode.com/problems/jump-game-ii/
from typing import List

from tester import Tester


class Solution:
    def jump(self, nums: List[int]) -> int:
        step = max_pos = 0
        tmp = nums[0]
        for i in range(1, len(nums)):
            if i > max_pos:
                step += 1
                max_pos = tmp
            tmp = max(tmp, i + nums[i])
        return step

# 7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3
# 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0
# 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 0
# 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2

# 3, 3, 1, 1, 4, 0
# 0, 1, 1, 1, 0, 0
# 0, 1, 1, 1, 2, 3

# 0 1 1 1 1 2 2 2 2 3 3 3 4 4 4 4 4
# 4 0 3 3 4 6 0 0 0 4 7 8 9 0 4 0 1

# 2, 3, 0, 1, 4
# 0  1  1
# 0  1  1  2  2


t = Tester(Solution())

t.test(2, [7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3])
t.test(3, [3, 5, 0, 3, 0, 0, 3, 0, 0, 0])
t.test(3, [3, 3, 1, 1, 4, 0])
t.test(2, [4, 3, 1, 1, 4, 0])
t.test(1, [5, 3, 1, 1, 4])
t.test(2, [2, 3, 1, 1, 4])
t.test(2, [2, 3, 0, 1, 4])
t.test(1, [5, 0])
t.test(0, [2])
t.test(0, [0])
t.test(0, [1])

t.report()