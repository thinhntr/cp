# https://leetcode.com/contest/weekly-contest-289/problems/calculate-digit-sum-of-a-string/
from typing import List
from tester import Tester


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            s = "".join(
                map(str, (sum(map(int, s[i : i + k])) for i in range(0, len(s), k)))
            )
        return s


t = Tester(Solution())

t.test("000", s="00000000", k=3)
t.test("135", s="11111222223", k=3)

t.report()
