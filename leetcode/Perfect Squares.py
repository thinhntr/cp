# https://leetcode.com/problems/perfect-squares/
from typing import List
from tester import Tester


class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i * i for i in range(1, int(n**0.5) + 1)]
        stack = {n}
        count = 1
        while stack:
            tmp = set()
            while stack:
                curr = stack.pop()
                for square in squares:
                    if square < curr:
                        tmp.add(curr - square)
                    if square == curr:
                        return count
            count += 1
            stack = tmp

        return count


t = Tester(Solution())

t.test(1, 1)
t.test(2, 2)
t.test(3, 3)
t.test(1, 4)
t.test(2, 5)
t.test(3, 12)
t.test(2, 13)

t.report()
