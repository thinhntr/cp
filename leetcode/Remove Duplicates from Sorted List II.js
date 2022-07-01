// https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

class ListNode {
  constructor(val, next) {
    this.val = val === undefined ? 0 : val
    this.next = next === undefined ? null : next
  }

  toString() {
    return `${this.val} - ${this.next?.toString()}`
  }
}

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function (head) {
  let h1 = null
  let h2 = head

  while (h2) {
    let h3 = h2.next

    while (h3 && h2.val === h3.val) {
      h3 = h3.next
    }

    if (h2.next === h3) {
      h1 = h2
    } else if (!h1) {
      head = h3
    } else {
      h1.next = h3
    }

    h2 = h3
  }

  return head
}

const root1 = new ListNode(
  1,
  new ListNode(
    2,
    new ListNode(
      3,
      new ListNode(3, new ListNode(4, new ListNode(4, new ListNode(5))))
    )
  )
)

console.log(root1.toString())

const root2 = deleteDuplicates(root1)

console.log(root2.toString())

const root3 = new ListNode(
  1,
  new ListNode(1, new ListNode(1, new ListNode(2, new ListNode(3))))
)

console.log(root3.toString())

const root4 = deleteDuplicates(root3)

console.log(root4.toString())

const root5 = new ListNode(
  5,
  new ListNode(
    6,
    new ListNode(7, new ListNode(8, new ListNode(8, new ListNode(8))))
  )
)

console.log(root5.toString())

const root6 = deleteDuplicates(root5)

console.log(root6.toString())
