# https://leetcode.com/problems/binary-search-tree-iterator/
from typing import Optional

from TreeNode import TreeNode
from TreeNode import list_to_treenodes as ltt
from tester import ObjectTester


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        stack = [root]
        while root.left:
            root = root.left
            stack.append(root)
        self.stack = stack

    def next(self) -> int:
        stack = self.stack
        val = stack[-1].val
        root = stack[-1].right
        if root:
            stack[-1] = root
            while root.left:
                root = root.left
                stack.append(root)
        else:
            stack.pop()
        return val

    def hasNext(self) -> bool:
        return not not self.stack

class BSTIterator:
    """Moris Traversal
    """
    def __init__(self, root: Optional[TreeNode]):
        self.curr = root

    def next(self) -> int:
        curr = self.curr
        # if curr:
        if not curr.left:
            self.curr = curr.right
            return curr.val

        tmp = curr.left
        while tmp.right and tmp.right != self.curr:
            tmp = tmp.right
        
        if not tmp.right:
            tmp.right = curr
            self.curr = curr.left
        else:
            tmp.right = None
            self.curr = curr.right
            return curr.val
        
        return self.next()

    def hasNext(self) -> bool:
        return not not self.curr


if __name__ == "__main__":
    o = ObjectTester(__file__)
    o.test(
        [None, 3, 7, True, 9, True, 15, True, 20, False],
        [
            "BSTIterator",
            "next",
            "next",
            "hasNext",
            "next",
            "hasNext",
            "next",
            "hasNext",
            "next",
            "hasNext",
        ],
        [[ltt("[7,3,15,null,null,9,20]")], [], [], [], [], [], [], [], [], []],
    )
    o.report()
