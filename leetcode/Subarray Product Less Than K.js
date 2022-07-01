// https://leetcode.com/problems/subarray-product-less-than-k/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var numSubarrayProductLessThanK = function (nums, k) {
  const N = nums.length

  let l = 0
  let count = 0
  let product = 1

  for (let r = 0; r < N; ++r) {
    product *= nums[r]

    while (product >= k && l <= r) {
      product /= nums[l]
      ++l
    }

    count += r - l + 1
  }

  return count
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

const t = new Tester(numSubarrayProductLessThanK)

t.test(8, [10, 5, 2, 6], 100)
t.test(0, [1, 2, 3], 0)

t.report()
