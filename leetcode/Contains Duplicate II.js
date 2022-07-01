// https://leetcode.com/problems/contains-duplicate-ii/

/**
 * Return true if there are two distinct indices i and j in the array 
 * such that nums[i] == nums[j] and abs(i - j) <= k.
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function (nums, k) {
  const cache = {}

  for (const [idx, num] of nums.entries()) {
    if (num in cache) {
      if (idx - cache[num] <= k) return true
      cache[num] = idx
    } else {
      cache[num] = idx
    }
  }

  return false
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

const t = new Tester(containsNearbyDuplicate)

t.test(true, [1, 2, 3, 1], 3)
t.test(true, [1, 0, 1, 1], 1)
t.test(false, [1, 2, 3, 1, 2, 3], 2)

t.report()
