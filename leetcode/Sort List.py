# https://leetcode.com/problems/sort-list/
from typing import Optional
from tester import Tester
from ListNode import ListNode, list_to_nodes

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def _split(self, head):
        tail = None
        slow = fast = head
        while fast and fast.next:
            tail = slow
            slow = slow.next
            fast = fast.next.next
        if tail:
            tail.next = None
        return head, slow

    def _merge(self, head):
        head1, head2 = self._split(head)

        if head1 == head2:
            return head1

        head1 = self._merge(head1)
        head2 = self._merge(head2)

        if head1.val < head2.val:
            head = head1
            head1 = head1.next
        else:
            head = head2
            head2 = head2.next

        tmp = head

        while head1 and head2:
            if head1.val < head2.val:
                tmp.next = head1
                head1 = head1.next
            else:
                tmp.next = head2
                head2 = head2.next
            tmp = tmp.next

        while head1:
            tmp.next = head1
            tmp = tmp.next
            head1 = head1.next

        while head2:
            tmp.next = head2
            tmp = tmp.next
            head2 = head2.next

        return head

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return list(self._merge(head))


t = Tester(Solution())

t.test([1, 2, 3, 4], list_to_nodes([4, 2, 1, 3]))
t.test([2, 3, 4, 5], list_to_nodes([5, 4, 3, 2]))
t.test([3, 4, 5], list_to_nodes([5, 4, 3]))
t.test([3, 5], list_to_nodes([5, 3]))
t.test([5], list_to_nodes([5]))

t.report()
