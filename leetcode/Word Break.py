# https://leetcode.com/problems/word-break/
from typing import List

from tester import Tester


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordDict = set(wordDict)
        dp = [None] * (n + 1)
        dp[n] = True

        def helper(i):
            if dp[i] is not None:
                return dp[i]
            for j in range(i + 1, n + 1):
                if s[i:j] in wordDict and helper(j):
                    dp[i] = True
                    return True
            dp[i] = False
            return False

        return helper(0)


t = Tester(Solution())

t.test(True, "leetcode", ["leet", "code"])
t.test(True, "applepenapple", ["apple", "pen"])
t.test(False, "catsandog", ["cats", "dog", "sand", "and", "cat"])

t.report()
