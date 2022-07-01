# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0
        for c in columnTitle:
            total = total * 26 + ord(c) - 64
        return total
        