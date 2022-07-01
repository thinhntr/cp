# https://leetcode.com/problems/longest-palindrome/
from typing import List
from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        freqs = defaultdict(lambda: 0)
        total = 0
        count_odd = 0
        for c in s:
            freqs[c] += 1
            if freqs[c] & 1:
                count_odd += 1
            else:
                total += 2
                count_odd = max(0, count_odd - 1)

        return total + 1 if count_odd else total


solution = Solution()


def check(input, expected):
    output = solution.longestPalindrome(input)
    assert output == expected


check("aaabbbyyyyy", 9)
check("abccccdd", 7)
check("aaabbb", 5)
check('a', 1)
check('bb', 2)
