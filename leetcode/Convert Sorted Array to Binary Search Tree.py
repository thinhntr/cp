# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'node({self.val}, {not not self.left}, {not not self.right})'


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def split(nums, l, r, root):
            m = (l + r) >> 1
            root.val = nums[m]

            if l <= m - 1:
                root.left = TreeNode()
                split(nums, l, m - 1, root.left)

            if m + 1 <= r:
                root.right = TreeNode()
                split(nums, m + 1, r, root.right)

            return root

        return split(nums, 0, len(nums) - 1, TreeNode())
