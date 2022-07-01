# https://leetcode.com/problems/increasing-order-search-tree/
from tester import Tester
from TreeNode import TreeNode
from TreeNode import list_to_treenodes as ltt


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        def iot(root):
            if root:
                iot(root.left)
                nodes.append(root)
                iot(root.right)
        iot(root)
        nodes.append(None)
        for a, b in zip(nodes, nodes[1:]):
            a.left = None
            a.right = b
        return nodes[0]


t = Tester(Solution())

t.test(ltt("[1,null,2,null,3,null,4]"), ltt("[2,1,4,null,null,3]"))
t.test(
    ltt("[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]"),
    ltt("[5,3,6,2,4,null,8,1,null,null,null,7,9]"),
)
t.test(ltt("[1,null,5,null,7]"), ltt("[5,1,7]"))

t.report()
