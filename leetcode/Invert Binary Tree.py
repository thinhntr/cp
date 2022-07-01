# https://leetcode.com/problems/invert-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root


solution = Solution()


def check(input, expected):
    output = solution.invertTree(input)
    assert output == expected

