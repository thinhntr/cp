# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l, r = 0, -1
        max_len = 0
        met_chars = set()

        for r in range(n):
            if s[r] in met_chars:
                while s[l] != s[r]:
                    met_chars.remove(s[l])
                    l += 1
                l += 1
            else:
                met_chars.add(s[r])
            max_len = max(max_len, r - l + 1)

        return max_len


solution = Solution()

assert solution.lengthOfLongestSubstring("abcabcbb") == 3
assert solution.lengthOfLongestSubstring("dvdf") == 3
assert solution.lengthOfLongestSubstring("advdf") == 3
