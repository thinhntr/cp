# https://leetcode.com/problems/ugly-number-ii/


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p2 = 0
        p3 = 0
        p5 = 0
        dp = [1] * n
        for i in range(1, n):
            p2val = dp[p2] * 2
            p3val = dp[p3] * 3
            p5val = dp[p5] * 5
            minval = min(p2val, p3val, p5val)
            if minval == p2val:
                p2 += 1
            if minval == p3val:
                p3 += 1
            if minval == p5val:
                p5 += 1
            dp[i] = minval
        return dp[n - 1]


solution = Solution()


def check(input, expected):
    output = solution.nthUglyNumber(input)
    assert output == expected


check(1, 1)
check(2, 2)
check(3, 3)
check(4, 4)
check(5, 5)
check(6, 6)
check(7, 8)
check(8, 9)
check(9, 10)
check(10, 12)
