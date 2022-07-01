# https://leetcode.com/problems/maximum-points-in-an-archery-competition/

from typing import List
from tester import Tester
from operator import itemgetter


class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        ns = sorted(zip(map(lambda x: x + 1, aliceArrows), range(12)))
        weight = list(map(itemgetter(0), ns))
        profit = list(map(itemgetter(1), ns))

        nrow = len(profit)
        ncol = numArrows + 1
        dp = [[0] * (ncol) for _ in range(nrow)]

        for c in range(ncol):
            if weight[0] <= c:
                dp[0][c] = profit[0]

        for i in range(1, nrow):
            for c in range(1, ncol):
                if c >= weight[i]:
                    dp[i][c] = max(dp[i - 1][c], profit[i] + dp[i - 1][c - weight[i]])
                else:
                    dp[i][c] = dp[i - 1][c]

        bob_arrows = [0] * 12
        score = dp[nrow - 1][numArrows]
        for i in reversed(range(1, nrow)):
            if score != dp[i - 1][numArrows]:
                bob_arrows[profit[i]] = weight[i]
                numArrows -= weight[i]
                score -= profit[i]
        if score:
            bob_arrows[profit[0]] = weight[0]
            numArrows -= weight[0]

        bob_arrows[0] = numArrows
        return bob_arrows


t = Tester(Solution())

t.test([0, 0, 0, 0, 1, 1, 0, 0, 1, 2, 3, 1], 9, [1, 1, 0, 1, 0, 0, 2, 1, 0, 1, 2, 0])
t.test([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0], 3, [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2])
t.test(
    [21, 3, 0, 2, 8, 2, 17, 8, 4, 14, 4, 6], 89, [3, 2, 28, 1, 7, 1, 16, 7, 3, 13, 3, 5]
)

t.test(
    [1947, 0, 1946, 13273, 8011, 6467, 13343, 2472, 14759, 8989, 6476, 4349],
    82032,
    [0, 1957, 1945, 13272, 8010, 6466, 13342, 2471, 14758, 8988, 6475, 4348],
)

t.report()
