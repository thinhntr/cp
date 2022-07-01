# https://leetcode.com/problems/letter-case-permutation/
from typing import List

from itertools import product


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        n = len(s)
        letter_indices = [i for i in range(n) if s[i].isalpha()]
        permutes = product([1,0], repeat=len(letter_indices))

        for permute in permutes:
            new_s = []
            prev_idx = 0
            for permute_idx, s_idx in enumerate(letter_indices):
                new_s.append(s[prev_idx:s_idx])
                prev_idx = s_idx + 1
                c = s[s_idx] # lbabl
                if permute[permute_idx]:
                    c = c.lower() if c.isupper() else c.upper()
                new_s.append(c)
            new_s.append(s[prev_idx:])
            result.append(''.join(new_s))

        return result


solution = Solution()


def check(inp, out):
    result = solution.letterCasePermutation(inp)
    assert len(result) == len(out) and set(result) == set(out)


check("a1b2", ["a1b2", "a1B2", "A1b2", "A1B2"])
check("3z4", ["3z4", "3Z4"])
check("12345", ["12345"])
check("0", ["0"])
