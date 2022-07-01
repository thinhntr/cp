# https://leetcode.com/problems/implement-queue-using-stacks/

from collections import deque


class MyQueue:
    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        result = self.peek()
        self.s2.pop()
        return result

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# 4 5 6 7
mq = MyQueue()
mq.push(1)
mq.push(2)
mq.push(3)
mq.push(4)
print(mq.pop())
mq.push(5)
print(mq.pop())
print(mq.pop())
print(mq.pop())
print(mq.pop())
# 1 2 3 4 5
# 7 6 5 4