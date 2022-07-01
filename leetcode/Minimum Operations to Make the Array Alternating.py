# https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/
from functools import reduce
from typing import List
from tester import Tester
from collections import Counter


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        len2 = len(nums) // 2
        len1 = len(nums) - len2
        counter1 = Counter(nums[::2])
        counter2 = Counter(nums[1::2])

        if not counter1 or not counter2:
            return 0
        
        count11 = max(counter1.values())
        count21 = max(counter2.values())

        num11 = set(filter(lambda num: counter1[num] == count11, counter1))
        num21 = set(filter(lambda num: counter2[num] == count21, counter2))

        if len(num11 - num21) or len(num21 - num11):
            return len1 - count11 + len2 - count21

        count12 = reduce(
            lambda a, b: b if b > a and b != count11 else a, counter1.values(), 0
        )
        count22 = reduce(
            lambda a, b: b if b > a and b != count21 else a, counter2.values(), 0
        )

        return min(len1 - count11 + len2 - count22, len1 - count12 + len2 - count21)


t = Tester(Solution())

t.test(0, [1])
t.test(2, [3, 3, 3, 4, 3, 3, 3])
t.test(1, [2, 2])
t.test(3, [3, 1, 3, 2, 4, 3])
t.test(2, [1, 2, 2, 2, 2])
t.test(3, [3, 3, 3, 4, 4, 4, 1])
t.test(6, [3, 3, 3, 3, 4, 4, 5, 5, 1])
t.test(3, [3, 3, 3, 3, 4, 4, 4])
t.test(
    51,
    [
        4,
        12,
        91,
        17,
        29,
        2,
        32,
        49,
        5,
        30,
        89,
        21,
        91,
        34,
        71,
        22,
        88,
        32,
        36,
        64,
        28,
        69,
        7,
        100,
        35,
        41,
        62,
        91,
        85,
        61,
        4,
        79,
        77,
        52,
        57,
        97,
        41,
        91,
        13,
        34,
        37,
        84,
        10,
        10,
        37,
        93,
        58,
        35,
        81,
        36,
        81,
        6,
        50,
        27,
        68,
    ],
)

t.report()
