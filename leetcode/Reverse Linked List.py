# https://leetcode.com/problems/reverse-linked-list/
from typing import Optional

from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self): return f'Node({self.val})'


class Solution:
    def reverse(self, current, prev):
        current_next = current.next
        current.next = prev
        return current if not current_next else self.reverse(current_next, current)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        return self.reverse(head, None)


node = ListNode

solution = Solution()
a = node(1, node(2, node(4)))
b = node(4, node(2, node(1)))


def compare_ll(a, b):
    while a and b:
        if a.val != b.val:
            return False
        a = a.next
        b = b.next
    return not a and not b


def check(a, b):
    result = solution.reverseList(a)
    assert compare_ll(result, b)


check(a, b)
check(None, None)
check(node(1), node(1))
check(node(1, node(2)), node(2, node(1)))
