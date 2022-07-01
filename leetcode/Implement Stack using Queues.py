# https://leetcode.com/problems/implement-stack-using-queues/
from collections import deque


class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        last_element = None
        while len(self.q1) > 1:
            last_element = self.q1.popleft()
            self.q2.append(last_element)
        last_element = self.q1.popleft()
        while self.q2:
            self.q1.append(self.q2.popleft())
        return last_element

    def top(self) -> int:
        last_element = None
        while self.q1:
            last_element = self.q1.popleft()
            self.q2.append(last_element)
        while self.q2:
            self.q1.append(self.q2.popleft())
        return last_element

    def empty(self) -> bool:
        return not self.q1 and not self.q2


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# 3 4 5 7 8

# 3 4 5 7 8
# 8 7 5 4 3
