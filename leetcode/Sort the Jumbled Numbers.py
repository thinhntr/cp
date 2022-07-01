# https://leetcode.com/contest/biweekly-contest-73/problems/sort-the-jumbled-numbers/
from operator import itemgetter
from typing import List
from tester import Tester


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def transform(num):
            if not num:
                return mapping[num]
            ten = 1
            result = 0
            while num:
                result = result + mapping[num % 10] * ten
                ten *= 10
                num //= 10
            return result

        transformed = [(i, transform(num)) for i, num in enumerate(nums)]
        transformed.sort(key=itemgetter(1))
        result = [nums[idx] for idx, _ in transformed]
        return result


t = Tester(Solution())

t.test([338, 38, 991], [8, 9, 4, 0, 2, 1, 3, 5, 7, 6], [991, 338, 38])
t.test([123, 456, 789], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [789, 456, 123])

t.report()
