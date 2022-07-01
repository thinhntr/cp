// https://leetcode.com/problems/contiguous-array/

/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxLength = function (nums) {
  const N = nums.length
  const prefixSum = nums.map((it) => (it !== 0 ? it : -1))

  for (let i = 1; i < N; ++i) {
    prefixSum[i] += prefixSum[i - 1]
  }

  let maxLen = 0
  const indices = new Map()

  // right - left = k => right - k = left
  for (let i = 0; i < N; ++i) {
    const left = prefixSum[i]

    if (!left) {
      maxLen = i + 1
    } else if (indices.has(left)) {
      maxLen = Math.max(maxLen, i - indices.get(left))
    } else {
      indices.set(left, i)
    }
  }

  return maxLen
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

const t = new Tester(findMaxLength)

t.test(0, [1])
t.test(0, [0])
t.test(2, [0, 1])
t.test(2, [1, 0])
t.test(2, [0, 1, 0])
t.test(2, [1, 0, 1])
t.test(4, [0, 1, 1, 1, 1, 0, 0])
t.test(4, [1, 1, 0, 0, 0, 0, 0, 1])
t.test(6, [1, 0, 1, 0, 0, 1])
t.test(6, [1, 0, 1, 0, 1, 0])

t.report()
