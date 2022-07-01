# https://leetcode.com/problems/implement-trie-prefix-tree/
from tester import ObjectTester


class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        t = self.trie
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t["-"] = True

    def search(self, word: str) -> bool:
        t = self.trie
        for c in word:
            if c not in t:
                return False
            t = t[c]
        return "-" in t

    def startsWith(self, prefix: str) -> bool:
        t = self.trie
        for c in prefix:
            if c not in t:
                return False
            t = t[c]
        return True


if __name__ == "__main__":
    o = ObjectTester(__file__)
    o.test(
        [None, None, True, False, True, None, True],
        ["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
        [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
    )
