# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)

        if not len_s:
            return True

        if len_s > len_t or not len_t:
            return False

        ps = pt = 0

        while ps < len_s and pt < len_t:
            if s[ps] == t[pt]:
                ps += 1
            pt += 1

        return ps == len_s and s[ps - 1] == t[pt - 1]

    def isSubsequence(self, s: str, t: str) -> bool:
        t = iter(t)
        return all(c in t for c in s)


solution = Solution()


def check(input, expected):
    output = solution.isSubsequence(*input)
    assert output == expected


check(["abc", "ahbgdc"], True)
check(["axc", "ahbgdc"], False)
check(["", "ahbgdc"], True)
check(["", ""], True)
check(["a", ""], False)
check(["acb", "ahbgdc"], False)
