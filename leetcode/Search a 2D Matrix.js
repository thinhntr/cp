// https://leetcode.com/problems/search-a-2d-matrix/

/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function (matrix, target) {
  const nrow = matrix.length
  const ncol = matrix[0].length

  let [l, r] = [0, nrow * ncol - 1]

  while (l <= r) {
    const m = Math.floor((l + r) / 2)
    const [i, j] = [Math.floor(m / ncol), m % ncol]
    // i*ncol+j

    if (matrix[i][j] === target) return true
    else if (matrix[i][j] < target) l = m + 1
    else r = m - 1
  }

  return false
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

const t = new Tester(searchMatrix)

t.test(
  true,
  [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60],
  ],
  3
)

t.test(
  false,
  [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60],
  ],
  13
)

t.report()
