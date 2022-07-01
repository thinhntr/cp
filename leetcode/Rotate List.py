# https://leetcode.com/problems/rotate-list/
from ListNode import ListNode, list_to_nodes as ltn
from typing import Optional
from tester import Tester


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return

        tmp = []
        while head:
            tmp.append(head)
            head = head.next

        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        n = len(tmp)
        if k:
            k %= n
            reverse(tmp, 0, n - k - 1)  # reverse the first n-k items
            reverse(tmp, n - k, n - 1)  # reverse the last k items
            reverse(tmp, 0, n - 1)  # reverse the entire array

        # fix link between nodes
        head = tmp[0]
        for node in tmp[1:]:
            head.next = node
            head = head.next
        tmp[-1].next = None
        return tmp[0]

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return

        tmp1 = []
        while head:
            tmp1.append(head)
            head = head.next

        n = len(tmp1)
        tmp2 = tmp1[:]
        if k:
            k %= n
            for i in range(n):
                tmp2[(i + k) % n] = tmp1[i]

        # fix link between nodes
        head = tmp2[0]
        for node in tmp2[1:]:
            head.next = node
            head = head.next
        tmp2[-1].next = None
        return tmp2[0]


t = Tester(Solution())

t.test(ltn("[5,1,2,3,4]"), ltn("[1,2,3,4,5]"), 1)
t.test(ltn("[4,5,1,2,3]"), ltn("[1,2,3,4,5]"), 2)
t.test(ltn(""), ltn(""), 0)
t.test(ltn("[0,1,2]"), ltn("[0,1,2]"), 0)
t.test(ltn("[2,0,1]"), ltn("[0,1,2]"), 1)
t.test(ltn("[1,2,0]"), ltn("[0,1,2]"), 2)
t.test(ltn("[0,1,2]"), ltn("[0,1,2]"), 3)
t.test(ltn("[2,0,1]"), ltn("[0,1,2]"), 4)

t.report()
