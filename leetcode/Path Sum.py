# https://leetcode.com/problems/path-sum/submissions/

from typing import Optional


# Definition for a binary tree node.
class node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        remain = targetSum - root.val

        if (not remain and not root.left and not root.right
                or self.hasPathSum(root.left, remain)):
            return True
        else:
            return self.hasPathSum(root.right, remain)


solution = Solution()


def check(input, expected):
    output = solution.hasPathSum(input[0], input[1])
    assert output == expected


root = node(1, node(2))
check([root, 1], False)
