# https://leetcode.com/problems/edit-distance/submissions/
from functools import lru_cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def next_state(p1, p2):
            min_dist = len(word1) + len(word2)

            # If p1 runs over word1
            if p1 >= len(word1):
                return len(word2) - p2

            # If p2 runs over word2
            if p2 >= len(word2):
                return len(word1) - p1

            # Match
            if word1[p1] == word2[p2]:
                min_dist = min(min_dist, next_state(p1 + 1, p2 + 1))

            # Insert
            min_dist = min(min_dist, next_state(p1, p2 + 1) + 1)

            # Delete
            min_dist = min(min_dist, next_state(p1 + 1, p2) + 1)

            # Replace
            min_dist = min(min_dist, next_state(p1 + 1, p2 + 1) + 1)

            return min_dist

        return next_state(0, 0)


solution = Solution()


def check(input, expected):
    output = solution.minDistance(input[0], input[1])
    assert output == expected


check(["horse", "ros"], 3)
check(["intention", "execution"], 5)
