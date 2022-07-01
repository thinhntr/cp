# https://leetcode.com/problems/largest-number/
from typing import List
from tester import Tester
import math
from functools import cmp_to_key


def compare(s1: str, s2: str) -> bool:
    if s1 == s2:
        return 0
    if s1 + s2 < s2 + s1:
        return 1
    return -1


compare = cmp_to_key(compare)


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(map(str, nums), key=compare)
        # found_none_zero = False
        for i, num in enumerate(nums):
            if nums[i] != "0":
                break
        return "".join(nums[i:]) if i < len(nums) else "0"


t = Tester(Solution())

t.test("9534330", [3, 30, 34, 5, 9])
t.test("210", [10, 2])
t.test("0", [0, 0])

t.report()
