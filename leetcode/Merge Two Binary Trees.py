# https://leetcode.com/problems/merge-two-binary-trees/
from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None

        if root1 and root2:
            root1.val += root2.val
            root1.left = self.mergeTrees(root1.left, root2.left)
            root1.right = self.mergeTrees(root1.right, root2.right)
            return root1

        return root1 if root1 else root2


def dfs(tree):
    if not tree:
        return
    print(tree.val)
    dfs(tree.left)
    dfs(tree.right)


def compare_tree(tree1, tree2):
    if not tree1 and not tree2:
        return True

    if tree1 and tree2:
        return (tree1.val == tree2.val
                and compare_tree(tree1.left, tree2.left)
                and compare_tree(tree1.right, tree2.right))

    return False


node = TreeNode

r1n1 = node(1)
root1 = r1n1
r1n3 = node(3)
r1n2 = node(2)
r1n5 = node(5)

r1n1.left = r1n3
r1n1.right = r1n2
r1n3.left = r1n5

# ----------------------------------------------------------------

r2n2 = node(2)
root2 = r2n2
r2n1 = node(1)
r2n3 = node(3)
r2n4 = node(4)
r2n7 = node(7)

r2n2.left = r2n1
r2n2.right = r2n3
r2n1.right = r2n4
r2n3.right = r2n7

# ----------------------------------------------------------------

root3 = node(3, node(4, node(5), node(4)), node(5, None, node(7)))

# ----------------------------------------------------------------

solution = Solution()

assert compare_tree(solution.mergeTrees(root1, root2), root3)

assert compare_tree(solution.mergeTrees(
    node(1), node(1, node(2))), node(2, node(2)))

result = solution.mergeTrees(
    node(1, node(2, node(3))), node(1, None, node(2, None, node(3))))
assert compare_tree(result, node(2, node(2, node(3)), node(2, None, node(3))))
