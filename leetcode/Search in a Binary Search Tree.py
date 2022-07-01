# https://leetcode.com/problems/search-in-a-binary-search-tree/
from typing import Optional
from tester import Tester
from operator import attrgetter
from TreeNode import TreeNode, list_to_treenodes as ltn


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if root.val == val:
                return root
            else:
                root = root.left if val < root.val else root.right
        return root


t = Tester(Solution())

t.test(ltn("[2,1,3]"), ltn("[4,2,7,1,3]"), 2)
t.test(None, ltn("[4,2,7,1,3]"), 5)

t.report()
