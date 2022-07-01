# https://leetcode.com/problems/split-array-largest-sum/
import operator
from itertools import accumulate
from typing import List

from tester import Tester


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        """Brute-force (DFS) Solution"""
        if m == 1:
            return sum(nums)
        if m == len(nums):
            return max(nums)

        prefix = list(accumulate(nums, operator.add))

        def sumrange(start, end):
            return prefix[end] - (prefix[start - 1] if start else 0)

        n = len(nums)

        dp = [[prefix[-1]] * m for _ in range(n)]

        for s in range(n):
            dp[s][0] = sumrange(s, n - 1)

        for c in range(1, m):
            for s in range(n - c):
                dp[s][c] = max(nums[s], dp[s + 1][c - 1])
                for i in range(s + 1, n - c):
                    dp[s][c] = min(dp[s][c], max(sumrange(s, i), dp[i + 1][c - 1]))

        return dp[0][m - 1]

    def splitArray(self, nums: List[int], m: int) -> int:
        """Binary Search Solution"""

        def can_split(largest):
            count = 1
            total = 0
            for num in nums:
                total += num
                if total > largest:
                    count += 1
                    total = num
            return count <= m

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = l + ((r - l) // 2)
            if can_split(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res


t = Tester(Solution())

t.test(4, [2, 3, 1, 2, 4, 3], 5)
t.test(18, [7, 2, 5, 10, 8], 2)
t.test(9, [1, 2, 3, 4, 5], 2)
t.test(4, [1, 4, 4], 3)

t.report()
