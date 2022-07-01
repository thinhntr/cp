# https://leetcode.com/problems/merge-two-sorted-lists/submissions/
from typing import Optional

from tester import Tester
from ListNode import ListNode, list_to_nodes as ltn


class Solution:
    def mergeTwoLists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode()
        tail = head
        while l1 and l2:
            if l1.val > l2.val:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next
            tail = tail.next
        tail.next = l1 or l2
        return head.next


t = Tester(Solution())

t.test(ltn("[1,1,2,3,4,4]"), ltn("[1,2,4]"), ltn("[1,3,4]"))

t.report()
