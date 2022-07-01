# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
from TreeNode import list_to_treenodes, TreeNode
from tester import Tester


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:

        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right


t = Tester(Solution())

tree = list_to_treenodes([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
nodes = list(tree)
t.test(nodes[1], tree, nodes[1], nodes[-1])
t.test(nodes[0], tree, nodes[1], nodes[2])

tree = list_to_treenodes([1,2])
nodes = list(tree)
t.test(nodes[0], tree, nodes[1], nodes[0])
t.report()
