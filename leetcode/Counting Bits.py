# https://leetcode.com/problems/counting-bits/
from typing import List
from tester import Tester


class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = [0] * (n + 1)
        for i in range(1, n + 1):
            counts[i] = counts[i >> 1] + (i & 1)
        return counts


t = Tester(Solution())

t.test([0, 1, 1], 2)
t.test([0, 1, 1, 2, 1, 2], 5)

t.report()

# 00000 0
# 00001 1
# 00010 1
# 00011 2

# 00100 1
# 00101 2
# 00110 2
# 00111 3

# 01000 1
# 01001 2
# 01010 2
# 01011 3

# 01100 2
# 01101 3
# 01110 3
# 01111 4

# 10000 1
# 10001 2
# 10010 2
# 10011 3

# 10100 2
# 10101 3
# 10110 3
# 10111 4

# 11000 2
# 11001 3
# 11010 3
# 11011 4

# 11100 3
# 11101 4
# 11110 4
# 11111 5

# 100000 1
# 100001 2
# 100010 2
# 100011 3

# 100100 2
# 100101 3
# 100110 3
# 100111 4

# 101000 2
# 101001 3
# 101010 3
# 101011 4
