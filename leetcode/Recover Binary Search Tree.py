# https://leetcode.com/problems/recover-binary-search-tree/
from typing import Optional

from tester import Tester
from TreeNode import TreeNode
from TreeNode import list_to_treenodes as ltt


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """Do not return anything, modify root in-place instead."""
        first = second = None
        prev = TreeNode(float("-inf"))

        def iot(root):
            nonlocal first, second, prev
            if not root:
                return
            iot(root.left)
            if prev.val > root.val:
                if not first:
                    first = prev
                if first:
                    second = root
            prev = root
            iot(root.right)

        iot(root)
        first.val, second.val = second.val, first.val
        return root


t = Tester(Solution())

t.test(ltt("[5,2,7]"), ltt("[5,7,2]"))
t.test(ltt("[3,1,null,null,2]"), ltt("[1,3,null,null,2]"))
t.test(ltt("[2,1,4,null,null,3]"), ltt("[3,1,4,null,null,2]"))
t.test(ltt("[5,2,7,null,null,6,8]"), ltt("[5,2,7,null,null,8,6]"))

t.report()
