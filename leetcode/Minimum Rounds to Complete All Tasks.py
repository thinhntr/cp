# https://leetcode.com/contest/weekly-contest-289/problems/minimum-rounds-to-complete-all-tasks/
from typing import Counter, List
from tester import Tester


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counts = Counter(tasks)
        max_count = max(counts.values())
        dp = [max_count + 1] * (max_count + 1)
        dp[0] = 0
        for c in (2, 3):
            for i in range(c, max_count + 1):
                dp[i] = min(dp[i], dp[i - c] + 1)
        total = 0
        for lvl, c in counts.items():
            if dp[c] == max_count + 1:
                return -1
            total += dp[c]
        return total


t = Tester(Solution())

t.test(4, [2, 2, 3, 3, 2, 4, 4, 4, 4, 4])  # 2: 3, 3: 2, 4: 5
t.test(-1, [2, 3, 3])

t.report()
