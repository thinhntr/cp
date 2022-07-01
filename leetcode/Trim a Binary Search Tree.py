# https://leetcode.com/problems/trim-a-binary-search-tree/
from typing import Optional

from tester import Tester
from TreeNode import TreeNode
from TreeNode import list_to_treenodes as ltt


class Solution:
    def trimBST(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> Optional[TreeNode]:
        if not root:
            return root

        if low > root.val:
            root = self.trimBST(root.right, low, high)
        elif high < root.val:
            root = self.trimBST(root.left, low, high)
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)

        return root


t = Tester(Solution())

t.test(ltt("[1,null,2]"), ltt("[1,0,2]"), 1, 2)
t.test(ltt("[3,2,null,1]"), ltt("[3,0,4,null,2,null,null,1]"), 1, 3)
t.test(ltt("[8,7,9]"), ltt("[5,2,8,1,3,7,9,null,null,null,4]"), 7, 9)
t.test(ltt("[5,3,7,null,4]"), ltt("[5,2,8,1,3,7,9,null,null,null,4]"), 3, 7)
t.test(ltt("[5,3,8,null,4,7]"), ltt("[5,2,8,1,3,7,9,null,null,null,4]"), 3, 8)
t.test(ltt("[5,3,8,null,4,7,9]"), ltt("[5,2,8,1,3,7,9,null,null,null,4]"), 3, 9)

t.report()
