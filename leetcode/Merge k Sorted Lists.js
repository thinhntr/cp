// https://leetcode.com/problems/merge-k-sorted-lists/

class ListNode {
  constructor(val, next) {
    this.val = val === undefined ? 0 : val
    this.next = next === undefined ? null : next
  }
}

class PriorityQueue {
  constructor() {
    this.queue = []
  }

  get length() {
    return this.queue.length
  }

  get isEmpty() {
    return !this.length
  }

  get isNotEmpty() {
    return !this.isEmpty
  }

  insertList(list) {
    while (list) {
      this.queue.push(list.val)
      this.bubbleUp(this.length - 1)
      list = list.next
    }
  }

  bubbleUp(i) {
    const parent = Math.floor(i / 2)

    if (this.queue[parent] > this.queue[i]) {
      const tmp = this.queue[i]
      this.queue[i] = this.queue[parent]
      this.queue[parent] = tmp
      this.bubbleUp(parent)
    }
  }

  bubbleDown(i) {
    let minIdx = i
    const child1 = i * 2
    const child2 = child1 + 1

    if (child1 < this.length && this.queue[minIdx] > this.queue[child1])
      minIdx = child1

    if (child2 < this.length && this.queue[minIdx] > this.queue[child2])
      minIdx = child2

    if (minIdx !== i) {
      const tmp = this.queue[i]
      this.queue[i] = this.queue[minIdx]
      this.queue[minIdx] = tmp
      this.bubbleDown(minIdx)
    }
  }

  pop() {
    if (this.isEmpty) return null

    const result = new ListNode(this.queue[0])

    this.queue[0] = this.queue[this.length - 1]
    this.queue.pop()
    this.bubbleDown(0)

    return result
  }
}

/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function (lists) {
  const queue = new PriorityQueue()

  for (const list of lists) {
    queue.insertList(list)
  }

  let root = queue.pop()
  let head = root

  while (queue.isNotEmpty) {
    head.next = queue.pop()
    head = head.next
  }

  return root
}

function arrayToLL(arr) {
  if (!arr.length) return null

  const root = new ListNode(arr[0])
  let head = root

  for (let i = 1; i < arr.length; ++i) {
    head.next = new ListNode(arr[i])
    head = head.next
  }

  return root
}

function llToArray(list) {
  const arr = []
  while (list) {
    arr.push(list.val)
    list = list.next
  }
  return arr
}

const l1 = arrayToLL([5, 18, 41])
const l2 = arrayToLL([1, 4, 5])
const l3 = arrayToLL([2, 6])

const l4 = mergeKLists([l1, l2, l3])
const a4 = llToArray(l4)

console.log(a4)
