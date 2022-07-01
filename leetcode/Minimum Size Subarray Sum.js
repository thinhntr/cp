// https://leetcode.com/problems/minimum-size-subarray-sum/

/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function (target, nums) {
  nums = [0, ...nums]
  const N = nums.length

  let l = 1
  let r = 1
  let minLen = N
  let sum = 0

  while (r < N) {
    sum = sum + nums[r] - nums[l - 1]

    while (sum < target && r < N - 1) {
      ++r
      sum += nums[r]
    }

    while (sum - nums[l] >= target && l < r) {
      sum -= nums[l]
      ++l
    }

    minLen = Math.min(minLen, r - l + 1)

    ++l
    ++r
  }

  return minLen === N - 1 && sum < target ? 0 : minLen
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

const t = new Tester(minSubArrayLen)

t.test(2, 7, [2, 3, 1, 2, 4, 3])
t.test(1, 4, [1, 4, 4])
t.test(0, 11, [1, 1, 1, 1, 1, 1, 1, 1])
t.test(5, 15, [1, 2, 3, 4, 5])
t.test(8, 213, [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12])

t.report()
