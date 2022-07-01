# https://leetcode.com/problems/generate-parentheses/

from typing import List
from tester import Tester


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def generate(n_open, n_close, s, result):
            if not n_open:
                result.append(s + ")" * n_close)
                return
            generate(n_open - 1, n_close, s + "(", result)
            if n_open < n_close:
                generate(n_open, n_close - 1, s + ")", result)

        generate(n, n, "", result)
        return result


s = Solution()
assert set(s.generateParenthesis(0)) == set([""])
assert set(s.generateParenthesis(1)) == set(["()"])
assert set(s.generateParenthesis(2)) == set(["()()", "(())"])
assert set(s.generateParenthesis(3)) == set(
    ["()()()", "()(())", "(())()", "(()())", "((()))"]
)

print(s.generateParenthesis(5))
