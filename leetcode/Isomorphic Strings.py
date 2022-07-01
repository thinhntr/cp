# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping1 = dict()
        mapping2 = dict()
        for si, ti in zip(s, t):
            if (si in mapping1 and mapping1[si] != ti
                    or ti in mapping2 and mapping2[ti] != si):
                return False
            else:
                mapping1[si] = ti
                mapping2[ti] = si
        return True


solution = Solution()


def check(input, expected):
    output = solution.isIsomorphic(input[0], input[1])
    assert output == expected


# print(solution.isIsomorphic("egg", "add"))
check(["egg", "add"], True)
check(["foo", "bar"], False)
check(["paper", "title"], True)
check(["bbbaaaba", "aaabbbba"], False)
check(["badc", "baba"], False)
