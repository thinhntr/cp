# https://leetcode.com/problems/add-two-numbers/
from typing import Optional
from ListNode import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0, ListNode(0))
        result = head
        remain = 0
        while l1 or l2:
            val = remain
            val += l1.val if l1 else 0
            val += l2.val if l2 else 0
            
            remain = 1 if val > 9 else 0
            val = val % 10
            
            result.next.val = val
            result.next.next = ListNode(0)
            result = result.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if remain:
            result.next.val = remain
        else:
            result.next = None
        return head.next
