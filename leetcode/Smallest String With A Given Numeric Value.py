# https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/
from tester import Tester
from string import ascii_lowercase

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = []
        for i in reversed(range(n)):
            idx = max(1, k - i * 26) - 1
            k -= idx + 1
            result.append(ascii_lowercase[idx])
        return ''.join(result)


t = Tester(Solution())

t.test("aay", 3, 27)
t.test("aaszz", 5, 73)

t.report()
