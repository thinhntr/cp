# https://leetcode.com/problems/count-artifacts-that-can-be-extracted/
from tester import Tester
from typing import List


class Solution:
    def digArtifacts(
        self, n: int, artifacts: List[List[int]], dig: List[List[int]]
    ) -> int:
        cells = [set() for _ in range(len(artifacts))]
        mapping = [[-1] * n for _ in range(n)]
        for k, a in enumerate(artifacts):
            for i in range(a[0], a[2] + 1):
                for j in range(a[1], a[3] + 1):
                    cells[k].add(i * n + j)
                    mapping[i][j] = k

        count = 0
        for i, j in dig:
            a_id = mapping[i][j]
            if not (0 <= a_id and a_id < len(cells)):
                continue
            cell = i * n + j
            if cell in cells[a_id]:
                cells[a_id].remove(cell)
            if not cells[a_id]:
                count += 1
        return count

t = Tester(Solution())

t.test(1, n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1]])
t.test(2, n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1],[1,1]])

t.report()