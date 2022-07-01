# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int, a=1, b=1) -> int:
        if not n:
            return a
        return self.climbStairs(n - 1, b, a + b)


solution = Solution()
print(solution.climbStairs(1))
print(solution.climbStairs(2))
print(solution.climbStairs(3))
print(solution.climbStairs(4))
print(solution.climbStairs(5))
print(solution.climbStairs(6))
