# https://leetcode.com/problems/score-of-parentheses/
from tester import Tester
from operator import add, mul

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [1, add, 0]
        for c in s[1:]:
            if c == "(":
                if len(stack) > 2 and stack[-2] != mul:
                    stack[-3] = 2
                    stack[-2] = mul
                    stack[-1] = 1
                    stack.append(add)
                    stack.append(0)
                else:
                    stack.extend([add, 1, add, 0])
                    
            else:
                num = stack.pop()
                op = stack.pop()
                stack[-1] = op(stack[-1], num)
                while len(stack) > 2 and stack[-2] == add:
                    num = stack.pop()
                    op = stack.pop()
                    stack[-1] = op(stack[-1], num)
        
        while len(stack) != 1:
            num = stack.pop()
            op = stack.pop()
            stack[-1] = op(stack[-1], num)

        return stack[0]


t = Tester(Solution())

t.test(16, "((()())(()()))")
t.test(14, "(((())())())")
t.test(1, "()")
t.test(2, "(())")
t.test(2, "()()")
t.test(12, "((()(())))")
t.test(12, "(((())()))")


t.report()
