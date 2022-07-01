# https://leetcode.com/problems/remove-k-digits/
from collections import deque
from itertools import islice
from tester import Tester


class MinSparseTable:
    def __init__(self, lst):
        ncol = len(lst)

        # Lookup table for floor(log2(i)), 1<=i<=N
        self.log2 = [0] * (ncol + 1)
        for i in range(2, ncol + 1):
            self.log2[i] = self.log2[i // 2] + 1

        # Number of rows in sparse table
        nrow = self.log2[ncol] + 1

        # Spare Table to find minimum values' index
        self.it = [[None] * ncol for _ in range(nrow)]
        self.it[0] = list(range(ncol))

        # Spare Table to find minimum values
        self.table = [[None] * ncol for _ in range(nrow)]
        self.table[0] = list(lst)

        # Fill the remaining rows
        for i in range(1, nrow):
            for j in range(ncol - (1 << i) + 1):
                left = self.table[i - 1][j]
                right = self.table[i - 1][j + (1 << (i - 1))]
                self.table[i][j] = min(left, right)

                self.it[i][j] = (
                    self.it[i - 1][j]
                    if left <= right
                    else self.it[i - 1][j + (1 << (i - 1))]
                )

    def __getitem__(self, pos):
        return self.table[0][pos]

    def min(self, l, r):
        return self[self.argmin(l, r)]

    def argmin(self, l, r):
        row = self.log2[r - l + 1]
        left = self.it[row][l]
        right = self.it[row][r - (1 << row) + 1]
        return left if self[left] <= self[right] else right


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if n == k:
            return "0"
        digits = list(num)
        mst = MinSparseTable(digits)
        r = n - k
        indices = deque()

        for end in reversed(range(1, r)):
            start = 0 if not indices else indices[-1] + 1
            # index = start + np.argmin(digits[start:-end])
            index = mst.argmin(start, n - end - 1)
            indices.append(index)

        start = 0 if not indices else indices[-1] + 1
        index = mst.argmin(start, n - 1)
        indices.append(index)

        # Remove leading zeros
        for i in range(len(indices)):
            if digits[indices[i]] != "0":
                break

        if i >= len(indices):
            return "0"

        return "".join(map(digits.__getitem__, islice(indices, i, None)))


t = Tester(Solution())

t.test("11", num="112", k=1)
t.test("1235", num="1239569", k=3)
t.test("0", num="1000", k=1)
t.test("0", num="1000", k=2)
t.test("2180", num="9725180", k=3)
t.test("2510", num="9725810", k=3)
t.test("1219", num="1432219", k=3)
t.test("200", num="10200", k=1)
t.test("0", num="10", k=2)
t.report()
