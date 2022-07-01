// https://leetcode.com/problems/largest-rectangle-in-histogram/

/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea = function (heights) {
  const N = heights.length
  const lessFromRight = Array(N).fill(N)
  const lessFromLeft = Array(N).fill(-1)

  let stack = []
  stack.push(0)

  // lessFromRight
  for (let i = 1; i < N; ++i) {
    while (stack.length && heights[stack[stack.length - 1]] > heights[i]) {
      lessFromRight[stack.pop()] = i
    }
    stack.push(i)
  }

  stack = []
  stack.push(N - 1)

  // lessFromLeft
  for (let i = N - 2; i >= 0; --i) {
    while (stack.length && heights[stack[stack.length - 1]] > heights[i]) {
      lessFromLeft[stack.pop()] = i
    }
    stack.push(i)
  }

  let area = 0

  for (let i = 0; i < N; ++i) {
    area = Math.max(area, heights[i] * (lessFromRight[i] - lessFromLeft[i] - 1))
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

const t = new Tester(largestRectangleArea)

t.test(10, [2, 1, 5, 6, 2, 3])
t.test(4, [2, 4])

t.report()
