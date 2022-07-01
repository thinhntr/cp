// https://leetcode.com/problems/find-peak-element/submissions/

/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function (nums) {
  if (nums.length === 1) return 0
  if (nums.length === 2) return nums[0] > nums[1] ? 0 : 1
  let [l, r] = [0, nums.length]

  while (l <= r) {
    const m = Math.floor((l + r) / 2)
    const mid = nums[m]

    if (nums[m - 1] < mid && mid > nums[m + 1]) {
      return m
    } else if (mid < nums[m + 1]) {
      l = m + 1
    } else {
      r = m - 1
    }
  }

  return l
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

const t = new Tester(findPeakElement)

t.test(2, [1, 2, 3, 1])
t.test(5, [1, 2, 1, 3, 5, 6, 4])
t.test(1, [4, 6, 5, 3, 1, 2, 1])
t.test(0, [1])

t.report()
