# https://leetcode.com/problems/spiral-matrix-iv/
from typing import List, Optional

from ListNode import ListNode
from ListNode import list_to_nodes as ltn
from tester import Tester


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat = [[-1] * n for _ in range(m)]
        top, bottom = 0, m
        left, right = 0, n
        while top < bottom or left < right:
            for i in range(left, right):
                if head:
                    mat[top][i] = head.val
                    head = head.next
                else:
                    break
            for i in range(top + 1, bottom):
                if head:
                    mat[i][right - 1] = head.val
                    head = head.next
                else:
                    break
            for i in range(right - 2, left - 1, -1):
                if head:
                    mat[bottom - 1][i] = head.val
                    head = head.next
                else:
                    break
            for i in range(bottom - 2, top, -1):
                if head:
                    mat[i][left] = head.val
                    head = head.next
                else:
                    break
            if not head:
                break
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return mat


t = Tester(Solution())

t.test([[0, 1, 2, -1]], m=1, n=4, head=ltn("[0,1,2]"))
t.test(
    [[3, 0, 2, 6, 8], [5, 0, -1, -1, 1], [5, 2, 4, 9, 7]],
    3,
    5,
    ltn("[3,0,2,6,8,1,7,9,4,2,5,5,0]"),
)
t.report()
