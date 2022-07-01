# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

from TreeNode import TreeNode, list_to_treenodes as ltn
# from tester  import Tester 


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original == target:
            return cloned
        if original.left:
            tmp = self.getTargetCopy(original.left, cloned.left, target)
            if tmp:
                return tmp
        if original.right:
            tmp = self.getTargetCopy(original.right, cloned.right, target)
            if tmp:
                return tmp
        return None


s = Solution()

a = ltn("[7,4,3,null,null,6,19]")
b = ltn("[7,4,3,null,null,6,19]")
t = a.right

assert s.getTargetCopy(a, b, t).val == t.val
print("success")
