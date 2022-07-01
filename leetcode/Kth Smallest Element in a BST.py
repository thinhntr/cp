# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
from typing import Optional

from tester import Tester
from TreeNode import TreeNode
from TreeNode import list_to_treenodes as ltt


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order = 0
        res = 0

        def iot(root):
            nonlocal res, order
            if not root:
                return
            iot(root.left)
            order += 1
            if order == k:
                res = root.val
            iot(root.right)

        iot(root)
        return res


t = Tester(Solution())

t.test(3, ltt("[2,null,4,3]"), 2)
t.test(1, ltt("[3,1,4,null,2]"), 1)
t.test(3, ltt("[5,3,6,2,4,null,null,1]"), 3)

t.report()
