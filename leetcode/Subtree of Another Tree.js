// https://leetcode.com/problems/subtree-of-another-tree/

/**
 * @param {TreeNode} r1
 * @param {TreeNode} r2
 * @return {boolean}
 */
function sameTree(r1, r2) {
  if (!r1 && !r2) return true
  if (r1 && r2 && r1.val === r2.val)
    return sameTree(r1.left, r2.left) && sameTree(r1.right, r2.right)
  return false
}

/**
 * @param {TreeNode} root
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
var isSubtree = function (root, subRoot) {
  if (!root && !subRoot) return true

  const stack = [root]

  while (stack.length) {
    const r = stack.pop()

    if (sameTree(r, subRoot)) return true

    if (r.left) stack.push(r.left)
    if (r.right) stack.push(r.right)
  }

  return false
}
