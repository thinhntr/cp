# https://leetcode.com/problems/unique-paths/


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        result = 1
        for i in range(0, m - 1):
            result *= (n + i) / (m - i - 1)
        return int(result + 0.5)


solution = Solution()


def check(input, expected):
    output = solution.uniquePaths(input[0], input[1])
    assert output == expected


# 1 <= m, n <= 100
check([7, 3], 28)
check([3, 7], 28)
check([3, 2], 3)
check([3, 3], 6)
check([9, 8], 6435)
check([10, 10], 48620)
