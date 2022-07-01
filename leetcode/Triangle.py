# https://leetcode.com/problems/triangle/
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        nr = len(triangle)
        min_length = triangle[-1][:]

        for r in reversed(range(nr - 1)):
            nc = len(triangle[r])
            for c in range(nc):
                r1 = r + 1
                min_length[c] = triangle[r][c] + \
                    min(triangle[r1][c], triangle[r1][c + 1])

        return min_length[0]


solution = Solution()

solution.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11
solution.minimumTotal([[-10]]) == -10
