# https://leetcode.com/problems/swap-nodes-in-pairs/

from typing import Optional
from ListNode import ListNode, list_to_nodes


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        h0 = None
        h1 = head
        root = head.next

        while h1 and h1.next:
            h2 = h1.next
            if h0:
                h0.next = h2
            # Swap
            h1.next = h2.next
            h2.next = h1
            # Next iterations
            h0 = h1
            h1 = h1.next if h1 else None

        return root

    def swapPairs(self, head: Optional[ListNode], prev=None) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        h1 = head
        h2 = head.next
        if prev:
            prev.next = h2
        # Swap
        h1.next = h2.next
        h2.next = h1

        self.swapPairs(h1.next, h1)

        return h2


s = Solution()

print(s.swapPairs(list_to_nodes([])))
print(s.swapPairs(list_to_nodes([1])))
print(s.swapPairs(list_to_nodes([1, 2])))
print(s.swapPairs(list_to_nodes([1, 2, 3])))
print(s.swapPairs(list_to_nodes([1, 2, 3, 4])))
print(s.swapPairs(list_to_nodes([1, 2, 3, 4, 5])))
print(s.swapPairs(list_to_nodes([1, 2, 3, 4, 5, 6])))
