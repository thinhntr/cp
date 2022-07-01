# https://leetcode.com/problems/word-ladder/


import string
from typing import List
from tester import Tester

from collections import deque


class Solution:
    def _replace(self, word, pos, char):
        new_str = list(word)
        new_str[pos] = char
        return "".join(new_str)

    def _get_neighbors(self, word):
        self.unvisited.discard(word)
        for i in range(len(word)):
            for letter in string.ascii_lowercase:
                new_word = self._replace(word, i, letter)
                if new_word in self.unvisited:
                    yield new_word

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.unvisited = set(wordList)
        begin = set([beginWord])
        end = set([endWord])

        if endWord not in self.unvisited:
            return 0

        length = 1
        while begin and end:
            if len(begin) > len(end):
                begin, end = end, begin

            tmp = set()
            while begin:
                cur_word = begin.pop()
                if cur_word in end:
                    return length
                for neighbor in self._get_neighbors(cur_word):
                    tmp.add(neighbor)

            begin = tmp
            length += 1

        return 0


t = Tester(Solution())

t.test(2, "b", "a", ["a"])
t.test(1, "a", "a", ["a"])
t.test(2, "a", "c", ["a", "b", "c"])
t.test(2, "a", "c", ["a", "b", "c", "d"])
t.test(0, "aa", "dd", ["aa", "bb", "cc"])
t.test(5, "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
t.test(5, "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog", "sot"])
t.test(0, "hit", "cog", ["hot", "dot", "dog", "lot", "log"])

t.report()
