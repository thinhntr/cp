# https://leetcode.com/problems/pascals-triangle/
from typing import List


class Solution:
    def generate(self, numRows) -> List[List[int]]:
        result = [[1]]
        for r in range(1, numRows):
            newRow = [1]
            lastRow = result[-1]
            for c in range(r - 1):
                newRow.append(lastRow[c] + lastRow[c + 1])
            newRow.append(1)
            result.append(newRow)
        return result


solution = Solution()


def check(input, expected):
    output = solution.generate(input)
    assert output == expected


check(5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])
check(1, [[1]])
