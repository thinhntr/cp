# https://leetcode.com/contest/weekly-contest-287/problems/find-players-with-zero-or-one-losses/
from typing import List
from tester import Tester


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        record = {}
        for winner, loser in matches:
            if loser in record:
                record[loser] += 1
            else:
                record[loser] = 1
            if winner not in record:
                record[winner] = 0

        result = [[], []]
        for player in record:
            if record[player] == 0:
                result[0].append(player)
            elif record[player] == 1:
                result[1].append(player)
        result[0].sort()
        result[1].sort()
        return result


t = Tester(Solution())

t.test(
    [[1, 2, 10], [4, 5, 7, 8]],
    [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]],
)
t.test([[1, 2, 5, 6], []], [[2, 3], [1, 3], [5, 4], [6, 4]])

t.report()
