# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
from ListNode import ListNode, list_to_nodes as ltn
from typing import Optional
from tester import Tester


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(next=head)
        prev = sentinel

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next
            
            head = head.next
        return sentinel.next


t = Tester(Solution())

head1 = ltn("[1,2,3,3,4,4,5]")
head2 = ltn("[1,2,5]")
t.test(head2, head1)

head1 = ltn("[1,1,1,2,3]")
head2 = ltn("[2,3]")
t.test(head2, head1)

t.report()
