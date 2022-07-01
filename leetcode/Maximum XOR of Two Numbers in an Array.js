// https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Node {
  constructor() {
    this.children = {}
  }
}

class Trie {
  constructor() {
    this.root = new Node()
  }

  insert(nums) {
    for (const num of nums) {
      let curr = this.root

      for (let i = 31; i >= 0; i--) {
        const currBit = (num >> i) & 1

        if (!(currBit in curr.children)) {
          curr.children[currBit] = new Node()
        }

        curr = curr.children[currBit]
      }
    }
  }
}

/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaximumXOR = function (nums) {
  const trie = new Trie()
  trie.insert(nums)

  let max = 0

  for (const num of nums) {
    let curr = trie.root
    let currSum = 0

    for (let i = 31; i >= 0; i--) {
      const requiredBit = 1 - ((num >> i) & 1)

      if (requiredBit in curr.children) {
        currSum = currSum | (1 << i)
        curr = curr.children[requiredBit]
      } else {
        curr = curr.children[1 - requiredBit]
      }

      max = Math.max(max, currSum)
    }
  }

  return max
}

findMaximumXOR = function (nums) {
  let max = 0
  let mask = 0

  for (let i = 31; i >= 0; --i) {
    mask = mask | (1 << i)
    const set = new Set()

    for (const num of nums) set.add(num & mask)

    const tmp = max | (1 << i)

    for (const prefix of set) {
      if (set.has(tmp ^ prefix)) {
        max = tmp
        break
      }
    }
  }

  return max
}

class Tester {
  constructor(fun) {
    this.fun = fun
    this.total = 0
    this.fail = 0
    this.time = 0
  }

  get pass() {
    return this.total - this.fail
  }

  test(expected, ...input) {
    const start = performance.now()
    const output = this.fun(...input)
    this.time += performance.now() - start

    const isCorrect = output === expected

    console.log('Test', this.total, '...', isCorrect)

    if (!isCorrect) {
      console.error('Output:', output)
      console.error('Expected:', expected)
      ++this.fail
    }

    console.log('')
    ++this.total
  }

  report() {
    console.log(`Passed ${this.pass} / ${this.total} tests
`)
    console.log(`Ran in ${this.time.toFixed(4)}ms`)
  }
}

const t = new Tester(findMaximumXOR)

t.test(28, [3, 10, 5, 25, 2, 8])
t.test(127, [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70])

t.report()
