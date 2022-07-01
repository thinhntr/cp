# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

from collections import deque

from TreeNode import TreeNode as Node
from TreeNode import list_to_treenodes as ltt


def add_next_prop(treenode):
    if not treenode:
        return
    treenode.next = None
    add_next_prop(treenode.left)
    add_next_prop(treenode.right)
    return treenode


class Solution:
    def connect(self, root: Node) -> Node:
        if not root or not root.left or not root.right:
            return root

        count, lvc = 1, 3
        stack = deque([root.left, root.right])
        while stack:
            node1 = stack.popleft()
            if node1.left:
                stack.append(node1.left)
                stack.append(node1.right)
            count += 1
            if count != lvc and stack:
                node1.next = stack[0]
            else:
                lvc = lvc * 2 + 1

        return root

    def connect(self, root):
        p = root
        n1 = n2 = root.left if root else None
        while n2:
            if n2 != p.left:
                n2.next = p.left
            else:
                n2.next = p.right
                p = p.next
            n2 = n2.next
            if not p:
                p, n1, n2 = n1, n1.left, n1.left
        return root


s = Solution()
root = add_next_prop(ltt("[1,2,3,4,5,6,7]"))
s.connect(root)
print(root)
