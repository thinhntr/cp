# https://leetcode.com/problems/permutation-in-string/

from collections import Counter
from copy import copy
from turtle import left


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counter1 = Counter(s1)
        counter2 = Counter()
        sublen = 0

        for r, right_char in enumerate(s2):
            # Add right char to counter2
            if right_char in counter1:
                if counter2[right_char] < counter1[right_char]:
                    sublen += 1
                counter2[right_char] += 1

            # Remove left char from counter2
            if len(s1) <= r:
                left_char = s2[r - len(s1)]
                if 0 < counter2[left_char]:
                    if counter2[left_char] <= counter1[left_char]:
                        sublen -= 1
                    counter2[left_char] -= 1

            # Check window
            if sublen == len(s1):
                return True

        return False


solution = Solution()
assert solution.checkInclusion("abc", "aicdbaooo") == False
assert solution.checkInclusion("abc", "aicdbcaooo") == True
assert solution.checkInclusion("abc", "accdbcaooo") == True
assert solution.checkInclusion("abc", "accdabooo") == False
assert solution.checkInclusion("abc", "accbabooo") == True
assert solution.checkInclusion("abc", "accbaeooo") == True
assert solution.checkInclusion("abcd", "acgebadco") == True
assert solution.checkInclusion("a", "acgebadco") == True
assert solution.checkInclusion("a", "cgebadco") == True
assert solution.checkInclusion("a", "cgebdca") == True
assert solution.checkInclusion("a", "cgebdc") == False
assert solution.checkInclusion("a", "ab") == True

assert solution.checkInclusion("ab", "eidbaooo") == True
assert solution.checkInclusion("ab", "eidboaoo") == False
assert solution.checkInclusion("adc", "dcda") == True
assert (
    solution.checkInclusion(
        "trinitrophenylmethylnitramine",
        "dinitrophenylhydrazinetrinitrophenylmethylnitramine",
    )
    == True
)
