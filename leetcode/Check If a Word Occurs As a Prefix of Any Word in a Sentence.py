# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
from tester import Tester


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        n = len(searchWord)
        for i, word in enumerate(sentence.split(" "), 1):
            if word[:n] == searchWord:
                return i
        return -1


t = Tester(Solution())

t.test(4, "i love eating burger", "burg")
t.test(2, "this problem is an easy problem", "pro")
t.test(-1, "i am tired", "you")

t.report()
