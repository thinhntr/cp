# https://leetcode.com/problems/nth-digit/

from tester import Tester


class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 9:
            return n
        i = 1
        ten = 1
        total = 9
        while total < n:
            i += 1
            ten *= 10
            total += i * 9 * ten
        total -= i * 9 * ten

        index = n - total - 1
        pos = index % i
        num = index // i + ten

        for i in range(i - 1 - pos):
            num //= 10
        return num % 10


t = Tester(Solution())

t.test(1, 1)
t.test(3, 3)
t.test(1, 10)
t.test(0, 11)
t.test(1, 190)
t.test(2, 198)


t.report()
