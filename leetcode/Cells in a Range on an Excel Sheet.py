# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/
from typing import List
from tester import Tester


def parse_cell(cell):
    for i in range(len(cell)):
        if cell[i].isnumeric():
            break
    col = 0
    for char in reversed(cell[:i]):
        col = col * 26 + ord(char) - 64
    row = int(cell[i:])
    return col, row


def serialize_cell(col, row):
    col_str = []
    while col:
        ascii_code = col % 26 + 64
        ascii_code += 26 if ascii_code < 65 else 0
        col_str.append(chr(ascii_code))
        col = col // 26 - 1 if col % 26 == 0 else 0
    return "".join(reversed(col_str)) + str(row)


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start, end = s.split(":")
        col_start, row_start = parse_cell(start)
        col_end, row_end = parse_cell(end)

        cells = []
        for col in range(col_start, col_end + 1):
            for row in range(row_start, row_end + 1):
                cells.append(serialize_cell(col, row))

        return cells


t = Tester(Solution())

t.test(["K1", "K2", "L1", "L2"], "K1:L2")
t.test(["A1","B1","C1","D1","E1","F1"], "A1:F1")
t.test(["P7","Q7","R7","S7","T7","U7","V7","W7","X7","Y7","Z7"], "P7:Z7")

t.report()
