# https://leetcode.com/problems/design-hashset/
from array import array
from itertools import repeat
from tester import ObjectTester


class MyHashSet:
    def __init__(self):
        self.arr = array('B')

    @property
    def n(self):
        return len(self.arr)

    def __extend(self, key):
        if key >= self.n:
            self.arr.extend(repeat(0, key - self.n + 1))

    def add(self, key: int) -> None:
        self.__extend(key)
        self.arr[key] = True

    def remove(self, key: int) -> None:
        self.__extend(key)
        self.arr[key] = False

    def contains(self, key: int) -> bool:
        return key < len(self.arr) and self.arr[key]


if __name__ == "__main__":
    o = ObjectTester(__file__)
    o.test(
        [None, None, None, True, False, None, True, None, False],
        [
            "MyHashSet",
            "add",
            "add",
            "contains",
            "contains",
            "add",
            "contains",
            "remove",
            "contains",
        ],
        [[], [1], [2], [1], [3], [2], [2], [2], [2]],
    )
    o.test(
        [None, None, None, None, None, None, None, None, None, None, None],
        [
            "MyHashSet",
            "add",
            "remove",
            "add",
            "remove",
            "remove",
            "add",
            "add",
            "add",
            "add",
            "remove",
        ],
        [[], [9], [19], [14], [19], [9], [0], [3], [4], [0], [9]],
    )
    o.report()
