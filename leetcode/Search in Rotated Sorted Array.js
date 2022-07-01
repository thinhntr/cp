// https://leetcode.com/problems/search-in-rotated-sorted-array/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  const len = nums.length
  let [l, r] = [0, len - 1]
  let end = len - 1

  while (
    nums[(end + len - 1) % len] >= nums[end] ||
    nums[end] <= nums[(end + 1) % len]
  ) {
    const m = Math.floor((l + r) / 2)
    const mid = nums[m]

    if (mid > nums[r]) {
      l = end = m
    } else if (mid < nums[r]) {
      r = end = m
    } else {
      end = m
      break
    }
  }

  if (target <= nums[len - 1]) {
    l = (end + 1) % len
    r = len - 1
  } else {
    l = 0
    r = end
  }

  while (l <= r) {
    const m = Math.floor((l + r) / 2)
    const mid = nums[m]

    if (mid === target) {
      return m
    } else if (mid < target) {
      l = m + 1
    } else {
      r = m - 1
    }
  }

  return -1
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

const t = new Tester(search)

t.test(4, [4, 5, 6, 7, 0, 1, 2], 0)
t.test(3, [4, 5, 6, 7, 0, 1, 2], 7)
t.test(5, [4, 5, 6, 7, 0, 1, 2], 1)
t.test(2, [4, 5, 6, 7, 0, 1, 2], 6)

t.test(1, [5, 6, 0, 1, 2, 3, 4], 6)
t.test(6, [0, 1, 2, 3, 4, 5, 6], 6)

t.test(-1, [4, 5, 6, 7, 0, 1, 2], 3)
t.test(-1, [1], 0)

t.test(2, [4, 5, 6, 7, 0, 1, 2], 6)

t.test(1, [3, 1], 1)
t.test(2, [2, 3, 1], 1)
t.test(3, [1, 2, 3, 0], 0)

t.report()
