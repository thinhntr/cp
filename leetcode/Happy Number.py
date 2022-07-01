# https://leetcode.com/problems/happy-number/
from typing import List


class Solution:
    def isHappy(self, n: int) -> bool:
        while n != 1:
            if 1 < n < 10:
                return False
            tmp = n
            n = 0
            while tmp:
                n += (tmp % 10) ** 2
                tmp //= 10
        return True


solution = Solution()


def check(input, expected):
    output = solution.isHappy(input)
    assert output == expected

check(19, True)
check(2, False)