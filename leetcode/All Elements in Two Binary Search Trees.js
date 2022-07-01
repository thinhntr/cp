// https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

function treeToArray(head) {
  if (!head) return []

  const arr = []
  const q = [head]

  while (q.length) {
    const top = q[q.length - 1]

    if (!top.left) {
      while (q.length) {
        const node = q.pop()
        arr.push(node.val)
        if (node.right) {
          q.push(node.right)
          break
        }
      }
    } else {
      q.push(top.left)
    }
  }

  return arr
}

/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {number[]}
 */
var getAllElements = function (root1, root2) {
  const result = []

  const a1 = treeToArray(root1)
  const a2 = treeToArray(root2)

  const n1 = a1.length
  const n2 = a2.length

  let i1 = 0
  let i2 = 0

  while (i1 < n1 && i2 < n2) {
    if (a1[i1] < a2[i2]) {
      result.push(a1[i1])
      ++i1
    } else {
      result.push(a2[i2])
      ++i2
    }
  }

  for (; i1 < n1; ++i1) result.push(a1[i1])
  for (; i2 < n2; ++i2) result.push(a2[i2])

  return result
}
