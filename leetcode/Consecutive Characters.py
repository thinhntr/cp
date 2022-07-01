# https://leetcode.com/problems/consecutive-characters/
from typing import List


class Solution:
    def maxPower(self, s):
        maxpow = 1
        pc = ''
        count = 1
        for c in s + ' ':
            if c != pc:
                maxpow = max(count, maxpow)
                pc = c
                count = 1
            else:
                count += 1
        return maxpow



solution = Solution()


def check(input, expected):
    output = solution.maxPower(input)
    assert output == expected

check("leetcode", 2)
check("abbcccddddeeeeedcba", 5)
check("triplepillooooow", 5)
check("hooraaaaaaaaaaay", 11)
check("tourist", 1)