# https://leetcode.com/problems/coin-change/
from typing import List
from tester import Tester


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        coins.sort()

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        """https://leetcode.com/problems/coin-change/discuss/1545305/BFS-with-Bit-Manipulation"""
        step, seen = 0, [amount]
        checked = set()
        while seen:
            cur = []
            for node in seen:
                if node == 0:
                    return step
                for coin in coins:
                    rem = node - coin
                    if rem >= 0 and rem not in checked:
                        cur.append(rem)
                        checked.add(rem)
            step, seen = step + 1, cur
        return -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        """Bitwise BFS."""
        step, seen = 0, 1 << amount
        while seen & 1 != 1:
            cur = seen
            for coin in coins:
                cur |= seen >> coin
            if cur == seen:
                return -1
            step, seen = step + 1, cur
        return step


t = Tester(Solution())

t.test(3, [1, 2, 5], 11)
t.test(-1, [2], 3)
t.test(0, [1], 0)

t.report()
