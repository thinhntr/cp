# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
from typing import Optional
from tester import Tester
from ListNode import ListNode, list_to_nodes as ltn


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """Time: O(n), Space: O(n)
        """
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        n = len(nodes)
        nodes[k - 1], nodes[n - k] = nodes[n - k], nodes[k - 1]
        for a, b in zip(nodes, nodes[1:]):
            a.next = b
        nodes[-1].next = None
        return nodes[0]

    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """Time: O(n), Space: O(1)
        """
        n1, n2, tmp = None, None, head
        while tmp:
            n2 = n2.next if n2 else None
            k -= 1
            if not k:
                n1 = tmp
                n2 = head
            tmp = tmp.next
        n1.val, n2.val = n2.val, n1.val
        return head


t = Tester(Solution())

t.test(ltn("[1]"), ltn("[1]"), 1)
t.test(ltn("[2,1]"), ltn("[1,2]"), 2)
t.test(ltn("[2,1]"), ltn("[1,2]"), 1)
t.test(ltn("[1,2,3]"), ltn("[3,2,1]"), 1)
t.test(ltn("[3,2,1]"), ltn("[3,2,1]"), 2)

t.report()
