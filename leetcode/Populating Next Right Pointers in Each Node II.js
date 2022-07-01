// https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

class Node {
  constructor(val, left, right, next) {
    this.val = val === undefined ? null : val
    this.left = left === undefined ? null : left
    this.right = right === undefined ? null : right
    this.next = next === undefined ? null : next
  }
}

/**
 * @param {Node} root
 * @return {Node}
 */
var connect = function (root) {
  if (!root) return root

  let queue = []

  if (root.left) queue.push(root.left)
  if (root.right) queue.push(root.right)

  while (queue.length) {
    const tmp = []
    let prev = null

    for (const curr of queue) {
      if (prev) {
        prev.next = curr
      }
      prev = curr
      if (curr.left) tmp.push(curr.left)
      if (curr.right) tmp.push(curr.right)
    }

    queue = tmp
  }
}
