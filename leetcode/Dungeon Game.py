# https://leetcode.com/problems/dungeon-game/
from typing import List
from tester import Tester


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dungeon[m - 1][n - 1] = max(1, 1 - dungeon[m - 1][n - 1])

        for i in range(m - 2, -1, -1):
            dungeon[i][-1] = max(1, dungeon[i + 1][-1] - dungeon[i][-1])

        for j in range(n - 2, -1, -1):
            dungeon[-1][j] = max(1, dungeon[-1][j + 1] - dungeon[-1][j])

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                curr = min(
                    dungeon[i][j + 1] - dungeon[i][j], dungeon[i + 1][j] - dungeon[i][j]
                )
                dungeon[i][j] = 1 if curr < 1 else curr
        return dungeon[0][0]


t = Tester(Solution())

t.test(1, [[0]])
t.test(7, [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])

t.report()
