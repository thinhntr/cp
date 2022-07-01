# https://leetcode.com/problems/unique-binary-search-trees/


class Solution:
    def numTrees(self, n: int) -> int:
        cache = {i: i for i in range(3)}
        cache[0] = 1

        def dp(l, r):
            size = r - l
            if size in cache:
                return cache[size]
            count = 0
            for m in range(l, r):
                tmp = 1
                tmp *= dp(l, m)
                tmp *= dp(m + 1, r)
                count += tmp
            cache[size] = count
            return count
        return dp(0, n)

    def numTrees(self, n: int) -> int:
        cache = [0] * (n + 1)
        cache[0] = cache[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                cache[i] += cache[j-1] * cache[i - j]
        return cache[n]


solution = Solution()


def check(input, expected):
    output = solution.numTrees(input)
    assert output == expected


check(1, 1)
check(2, 2)
check(3, 5)
check(4, 14)
check(5, 42)
check(6, 132)
