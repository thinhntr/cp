# https://leetcode.com/problems/min-stack/

from collections import deque

class MinStack:

    def __init__(self):
        self.stack = deque()

    @property
    def is_empty(self):
        return not len(self.stack) != 0

    def push(self, val: int) -> None:
        new_min = val if self.is_empty else min(self.getMin(), val)
        self.stack.append((val, new_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

ms = MinStack()
ms.push(4)
print(ms.top(), ms.getMin())
ms.push(5)
print(ms.top(), ms.getMin())