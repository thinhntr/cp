# https://leetcode.com/problems/convert-bst-to-greater-tree/
from typing import Optional

from tester import Tester
from TreeNode import TreeNode
from TreeNode import list_to_treenodes as ltt


class Solution:
    def convertBST(
        self, root: Optional[TreeNode], total: int = 0
    ) -> Optional[TreeNode]:
        def accumulate(root, total):
            if root.right:
                root.val += accumulate(root.right, total)
            else:
                root.val += total
            if root.left:
                return accumulate(root.left, root.val)
            return root.val

        if root:
            accumulate(root, 0)
        return root


t = Tester(Solution())

t.test(
    ltt("[39,45,24,45,44,30,17,null,null,null,42,35,null,null,9]"),
    ltt("[4,1,7,0,2,6,8,null,null,null,3,5,null,null,9]"),
)
t.test(
    ltt("[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]"),
    ltt("[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]"),
)
t.test(ltt("[1,null,1]"), ltt("[0,null,1]"))

t.report()
