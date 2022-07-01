// https://leetcode.com/problems/container-with-most-water/
/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  const N = height.length
  let area = 0
  let l = 0
  let r = N - 1

  while (l < r) {
    area = Math.max(area, Math.min(height[l], height[r]) * (r - l))
    if (height[r] > height[l]) ++l
    else --r
  }

  return area
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

const t = new Tester(maxArea)

t.test(49, [1, 8, 6, 2, 5, 4, 8, 3, 7])
t.test(1, [1, 1])
t.test(0, [0, 2])

t.report()
