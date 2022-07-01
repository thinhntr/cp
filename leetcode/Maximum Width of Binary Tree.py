# https://leetcode.com/problems/maximum-width-of-binary-tree/

from collections import deque
from typing import Optional

from tester import Tester
from TreeNode import TreeNode, list_to_treenodes as ltt


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxwidth = 1
        queue = deque([(root, 1)])
        while queue:
            n = len(queue)
            maxwidth = max(maxwidth, queue[-1][1] - queue[0][1] + 1)
            for _ in range(n):
                node, count = queue.popleft()
                child = count << 1
                if node.left:
                    queue.append((node.left, child))
                if node.right:
                    queue.append((node.right, child + 1))
        return maxwidth


t = Tester(Solution())

t.test(8, ltt("[1,3,2,5,null,null,9,6,null,null,7]"))
t.test(7, ltt("[1,3,2,5,null,null,9,6,null,7]"))
t.test(4, ltt("[1,3,2,5,3,null,9]"))
t.test(2, ltt("[1,3,null,5,3]"))
t.test(2, ltt("[1,3,2,5]"))

t.report()
