// https://leetcode.com/problems/3sum/

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  nums.sort((a, b) => a - b)

  const res = []
  const N = nums.length

  for (let i = 0; i < N; ++i) {
    const target = -nums[i]
    let start = i + 1
    let end = N - 1

    while (start < end) {
      const sum = nums[start] + nums[end]

      if (sum < target) ++start
      else if (sum > target) --end
      else {
        const num2 = nums[start]
        const num3 = nums[end]
        res.push([nums[i], num2, num3])
        
        while (num2 === nums[start]) ++start
        while (num3 === nums[end]) --end
      }
    }

    while (nums[i] === nums[i + 1]) ++i
  }

  return res
}

function compareArray(a, b) {
  if (a === b) return true
  if (a.length !== b.length) return false

  for (const [idx, val] of a.entries()) {
    const other = b[idx]
    if (typeof val !== typeof other) return false
    if (val instanceof Array) {
      if (!compareArray(val, other)) return false
    } else {
      if (val !== other) return false
    }
  }

  return true
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

    const isCorrect = compareArray(output, expected)

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

const t = new Tester(threeSum)

t.test(
  [
    [-1, -1, 2],
    [-1, 0, 1],
  ],
  [-1, 0, 1, 2, -1, -4]
)

t.test([], [])

t.test([], [0])

t.report()
