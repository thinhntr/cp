// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function (nums) {
  let [l, r] = [0, nums.length - 1]

  while (l < r) {
    const m = Math.floor((l + r) / 2)

    if (nums[m] > nums[r]) l = m + 1
    else r = m
  }

  return nums[l]
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

const t = new Tester(findMin)

t.test(1, [3, 4, 5, 1, 2])
t.test(1, [5, 1, 2, 3, 4])
t.test(0, [4, 5, 6, 7, 0, 1, 2])
t.test(11, [11, 13, 15, 17])
t.test(1, [3, 1, 2])

t.report()
