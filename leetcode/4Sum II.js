// https://leetcode.com/problems/4sum-ii/

/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @param {number[]} nums3
 * @param {number[]} nums4
 * @return {number}
 */
var fourSumCount = function (nums1, nums2, nums3, nums4) {
  const N = nums1.length
  const counter34 = new Map()

  for (let i = 0; i < N; ++i) {
    for (let j = 0; j < N; ++j) {
      const sum = nums3[i] + nums4[j]
      counter34.set(sum, 1 + (counter34.get(sum) ?? 0))
    }
  }

  let count = 0

  for (let i = 0; i < N; ++i) {
    for (let j = 0; j < N; ++j) {
      const remain = -nums1[i] - nums2[j]
      count += counter34.get(remain) ?? 0
    }
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

const t = new Tester(fourSumCount)

t.test(1, [0], [0], [0], [0])
t.test(0, [0], [1], [0], [0])
t.test(0, [0], [1], [0], [3])
t.test(6, [-1, -1], [-1, 1], [-1, 1], [1, -1])
t.test(2, [1, 2], [-2, -1], [-1, 2], [0, 2])
t.test(17, [0, 1, -1], [-1, 1, 0], [0, 0, 1], [-1, 1, 1])

t.report()
