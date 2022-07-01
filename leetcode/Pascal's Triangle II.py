# https://leetcode.com/problems/pascals-triangle-ii/
from typing import List


class Solution:
    def getRow(self, rowIndex) -> List[int]:
        result = [1]
        for r in range(rowIndex):
            newRow = [1]
            for c in range(r):
                newRow.append(result[c] + result[c + 1])
            newRow.append(1)
            result = newRow
        return result


solution = Solution()


def check(input, expected):
    output = solution.getRow(input)
    assert output == expected

check(0, [1])
check(1, [1, 1])
check(2, [1, 2, 1])
check(3, [1,3,3,1])