# https://leetcode.com/problems/smallest-number-in-infinite-set/
from typing import Optional

from tester import ObjectTester


class SmallestInfiniteSet:
    def __init__(self):
        self.smallest = 1
        self.exclude = set()

    def popSmallest(self) -> int:
        res = self.smallest
        self.smallest += 1
        while self.smallest in self.exclude:
            self.smallest += 1
        self.exclude.add(res)
        return res

    def addBack(self, num: int) -> None:
        if num in self.exclude:
            self.exclude.remove(num)
            if num < self.smallest:
                self.smallest = num


if __name__ == "__main__":
    o = ObjectTester(__file__)
    o.test(
        [None, None, 1, 2, 3, None, 1, 4, 5],
        [
            "SmallestInfiniteSet",
            "addBack",
            "popSmallest",
            "popSmallest",
            "popSmallest",
            "addBack",
            "popSmallest",
            "popSmallest",
            "popSmallest",
        ],
        [[], [2], [], [], [], [1], [], [], []],
    )
    o.report()
