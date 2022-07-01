// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function (nums, target) {
  const n = nums.length

  if (n < 1) return [-1, -1]

  let [start, end] = [-1, -1]
  let [l, r] = [0, n - 1]

  while (l <= r) {
    const m = Math.floor((l + r) / 2)
    const mid = nums[m]

    if (mid < target) l = m + 1
    else if (target < mid || (m - 1 >= 0 && nums[m - 1] === mid)) r = m - 1
    else {
      start = end = m
      break
    }
  }

  ;[l, r] = [start + 1, n - 1]

  while (l <= r) {
    const m = Math.floor((l + r) / 2)
    const mid = nums[m]

    if (target < mid) r = m - 1
    else if (mid < target || (m + 1 < n && nums[m + 1] === mid)) l = m + 1
    else {
      end = m
      break
    }
  }

  return [start, end]
}

// console.debug('start')
// console.debug(searchRange([5, 7, 7, 8, 8, 10], 8))
// console.debug('end')

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

  compareArray(a, b) {
    if (a === b) return true
    if (a.length !== b.length) return false
    for (let i = 0; i < a.length; ++i) {
      if (a[i] !== b[i]) return false
    }
    return true
  }

  test(expected, ...input) {
    const start = performance.now()
    const output = this.fun(...input)
    this.time += performance.now() - start

    const isCorrect = this.compareArray(output, expected)

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

const t = new Tester(searchRange)

t.test([3, 4], [5, 7, 7, 8, 8, 10], 8)
t.test([1, 2], [5, 7, 7, 8, 8, 10], 7)
t.test([1, 4], [5, 7, 7, 7, 7, 10], 7)
t.test([1, 5], [5, 7, 7, 7, 7, 7, 10], 7)
t.test([2, 5], [5, 6, 7, 7, 7, 7, 10], 7)
t.test([0, 3], [7, 7, 7, 7, 10], 7)
t.test([1, 4], [1, 7, 7, 7, 7], 7)
t.test([2, 6], [5, 6, 7, 7, 7, 7, 7, 10], 7)
t.test([-1, -1], [5, 7, 7, 7, 7, 10], 8)
t.test([-1, -1], [5, 7, 7, 8, 8, 10], 6)
t.test([-1, -1], [], 0)

t.report()
