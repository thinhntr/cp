// https://leetcode.com/problems/number-of-provinces/

/**
 * @param {number[][]} isConnected
 * @return {number}
 */
var findCircleNum = function (isConnected) {
  const N = isConnected.length
  const visited = new Set()
  let count = 0

  for (let id = 0; id < N; ++id) {
    if (visited.has(id)) continue

    visited.add(id)
    ++count

    const queue = [id]

    while (queue.length) {
      const front = queue.pop()

      for (let j = 0; j < N; ++j) {
        if (!isConnected[front][j] || visited.has(j)) continue
        visited.add(j)
        queue.push(j)
      }
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

const t = new Tester(findCircleNum)

t.test(2, [
  [1, 1, 0],
  [1, 1, 0],
  [0, 0, 1],
])

t.test(3, [
  [1, 0, 0],
  [0, 1, 0],
  [0, 0, 1],
])

t.report()
