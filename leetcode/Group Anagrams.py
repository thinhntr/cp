# https://leetcode.com/problems/group-anagrams/
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        ord_a = ord("a")
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord_a] += 1
            groups[tuple(counter)].append(s)
        return list(groups.values())


tests = [
    ["eat", "tea", "tan", "ate", "nat", "bat"],
    ["ac", "c"],
    ["ac", "d"],
    [""],
    ["a"],
]
expected_vals = [
    [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
    [["ac"], ["c"]],
    [["ac"], ["d"]],
    [[""]],
    [["a"]],
]

s = Solution()
for test, expected in zip(tests, expected_vals):
    output = s.groupAnagrams(test)
    print(output)
    print(expected)
    print()
