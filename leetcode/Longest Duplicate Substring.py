# https://leetcode.com/problems/longest-duplicate-substring/
from typing import List
from collections import defaultdict


class Solution:
    def longestSubstring(self, s: str) -> str:
        result = ''
        prev_indices = defaultdict(lambda: [])
        n = len(s)
        max_len = 0
        for i, c in enumerate(s):
            for prev_idx in prev_indices[c]:
                tmp_i = i
                while i < n and s[prev_idx] == s[i]:
                    prev_idx += 1
                    i += 1
                cur_len = i - tmp_i
                if cur_len > max_len:
                    result = s[tmp_i:i]
                    max_len = cur_len

            prev_indices[c].append(i)
        return result

solution = Solution()


def check(input, expected):
    output = solution.longestSubstring(input)
    assert output == expected


check("banana", "ana")
check("bana", "a")
check("abcd", "")
check("aaaaaaaaabaaaaaaaa", 'aaaaaaaa')
check("aaaaaaaaaabaaaaaaaa", 'aaaaaaaaa')
