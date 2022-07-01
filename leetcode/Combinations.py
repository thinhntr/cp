# https://leetcode.com/problems/combinations/
from typing import List

class Solution:
    def somefun(self, result, current, remain, n, k):
        if k == 0:
            result.append(current)
            return

        current.append(0)
        for i in range(n - k + 1):
            current[-1] = remain[i]
            self.somefun(result, current[:], remain[i + 1:], n - i - 1, k - 1)

    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        remain = list(range(1, n + 1))
        self.somefun(result, [], remain, n, k)
        return result


solution = Solution()


def to_set(ll):
    return set(map(tuple, ll))


def check(n, k, output):
    result = solution.combine(n, k)
    assert len(result) == len(output) and to_set(result) == to_set(output)


check(1, 0, [[]])
check(2, 0, [[]])
check(1, 1, [[1]])
check(2, 2, [[1, 2]])
check(3, 3, [[1, 2, 3]])
check(4, 4, [[1, 2, 3, 4]])
check(4, 2, [[2, 4],
             [3, 4],
             [2, 3],
             [1, 2],
             [1, 3],
             [1, 4], ])
check(5, 3, [[1, 2, 3],
             [1, 2, 4],
             [1, 2, 5],
             [1, 3, 4],
             [1, 3, 5],
             [1, 4, 5],
             [2, 3, 4],
             [2, 3, 5],
             [2, 4, 5],
             [3, 4, 5], ])
