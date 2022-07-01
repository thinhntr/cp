# https://leetcode.com/problems/remove-duplicate-letters/
from tester import Tester


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_idxs = {}
        for i, c in enumerate(s):
            last_idxs[c] = i

        stack = []
        visited = set()
        for i, c in enumerate(s):
            if not stack:
                visited.add(c)
                stack.append(c)
            if c in visited:
                continue
            while stack and c < stack[-1]:
                if i >= last_idxs[stack[-1]]:
                    break
                visited.remove(stack.pop())
            stack.append(c)
            visited.add(c)
        return "".join(stack)


t = Tester(Solution())

t.test("abcd", "bcabcd")
t.test("abcd", "bcabcad")
t.test("abc", "bcabc")
t.test("acdb", "cbacdcbc")

t.report()
