// https://leetcode.com/problems/contains-duplicate-iii/

/**
 * Return true if there are two distinct indices i and j in the array
 * such that abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.
 * @param {number[]} nums
 * @param {number} k
 * @param {number} t
 * @return {boolean}
 */
var containsNearbyAlmostDuplicate = function (nums, k, t) {
  const bucketSize = t + 1
  const buckets = new Map()

  for (const [i, num] of nums.entries()) {
    const addr = Math.floor(num / bucketSize)

    if (
      buckets.has(addr) ||
      (buckets.has(addr - 1) && num - buckets.get(addr - 1) <= t) ||
      (buckets.has(addr + 1) && buckets.get(addr + 1) - num <= t)
    ) {
      return true
    } else {
      buckets.set(addr, num)
      if (buckets.size > k) {
        const addrToDelete = Math.floor(nums[i - k] / bucketSize)
        buckets.delete(addrToDelete)
      }
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
      console.error('Input:', input)
      console.error('Output:', output)
      console.error('Expected:', expected)
      ++this.fail
    }

    console.log('')
    ++this.total
  }

  report() {
    console.log(`Passed ${this.pass} / ${this.total} tests\n`)
    console.log(`Ran in ${this.time.toFixed(4)}ms`)
  }
}

const t = new Tester(containsNearbyAlmostDuplicate)

t.test(true, [1, 2, 3, 1], 3, 0)
t.test(true, [1, 0, 1, 1], 1, 2)
t.test(true, [3, 6, 0, 4], 2, 2)
t.test(true, [1, 1, 5], 3, 0)
t.test(true, [5, 1, 1], 3, 0)
t.test(false, [1, 5, 9, 1, 5, 9], 2, 3)
t.test(true, [-1, -2, 5], 1, 1)

t.report()
