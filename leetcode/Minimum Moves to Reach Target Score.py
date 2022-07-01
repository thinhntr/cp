from collections import deque
from tester import Tester


class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0
        while target != 1 and maxDoubles:
            if target % 2 == 0:
                target //= 2
                maxDoubles -= 1
            else:
                target -= 1
            count += 1
        return count + target - 1


t = Tester(Solution())

t.test(7, 19, 2)
t.test(4, 10, 4)
t.test(4, 5, 0)
t.test(45, 766972377, 92)
t.test(328050994, 656101987, 1)

t.report()
