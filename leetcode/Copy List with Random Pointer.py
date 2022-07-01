#
from collections import deque
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return head

        cloneof = {None: None, head: Node(head.val)}
        queue = [head]
        while queue:
            curr = queue.pop()
            if not curr:
                continue
            next = curr.next
            random = curr.random
            node = cloneof[curr]

            if next and next not in cloneof:
                cloneof[next] = Node(next.val)
                queue.append(next)
            node.next = cloneof[next]

            if random and random not in cloneof:
                cloneof[random] = Node(random.val)
                queue.append(random)
            node.random = cloneof[random]

        return cloneof[head]
