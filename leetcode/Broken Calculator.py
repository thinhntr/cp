# https://leetcode.com/problems/broken-calculator/
from tester import Tester


class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        """BFS Solution
        """
        count = 0
        queue = {startValue}
        while queue:
            if target in queue:
                return count

            tmp = set()
            while queue:
                curr = queue.pop()
                tmp.add(curr * 2)
                tmp.add(curr - 1)
            queue = tmp
            count += 1
        return count

    def brokenCalc(self, startValue: int, target: int) -> int:
        """Greedy solution
        """
        count = 0
        while target > startValue:
            if target % 2 == 0:
                target >>= 1
            else:
                target += 1
            count += 1
        return count + startValue - target


t = Tester(Solution())

t.test(2, 2, 3)
t.test(2, 5, 8)
t.test(3, 3, 10)
t.test(6, 3, 13)
t.test(0, 4, 4)

t.report()
