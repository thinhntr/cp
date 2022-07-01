# https://leetcode.com/problems/best-sightseeing-pair/
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        self.values = values
        l, r = 0, 1
        max_val = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                val = values[i] + values[j] + i - j
                if val > max_val:
                    max_val = val
                    l, r = i, j
        return values[l] + values[r] + l - r

    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        i, j = 0, 1
        max_sum = values[j] + values[i] - j + i
        cur_sum = max_sum

        for k in range(2, n):
            ik_sum = values[k] + values[i] - k + i
            jk_sum = values[k] + values[j] - k + j

            if ik_sum > jk_sum:
                j = k
                cur_sum = ik_sum
            else:
                i, j = j, k
                cur_sum = jk_sum

            if cur_sum > max_sum:
                max_sum = cur_sum

        return max_sum

    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        curr_max = max(values[0], values[1] + 1)
        max_score = values[0] + values[1] - 1
        for i in range(2, len(values)):
            new_score = curr_max + values[i] - i
            new_max = values[i] + i
            if new_score > max_score:
                max_score = new_score
            if new_max > curr_max:
                curr_max = new_max
        return max_score


solution = Solution()


def check(inp, expected):
    output = solution.maxScoreSightseeingPair(inp)
    assert output == expected


check([8, 1, 5, 2, 6], 11)
check([1, 2], 2)
check([8, 9, 1, 10, 2, 9], 17)
check([1, 2, 1, 4, 3, 1, 1, 1, 1, 1, 10, 12, 1], 21)
check([1, 2, 1, 4, 5, 1, 1, 1, 1, 1, 10, 12, 1], 21)
