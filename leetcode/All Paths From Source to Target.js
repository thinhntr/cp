// https://leetcode.com/problems/all-paths-from-source-to-target/

/**
 * @param {number[][]} graph
 * @return {number[][]}
 */
var allPathsSourceTarget = function (graph, start = 0) {
  if (start === graph.length - 1) return [[graph.length - 1]]

  const result = []

  for (const neighbor of graph[start]) {
    const paths = allPathsSourceTarget(graph, neighbor)
    for (const path of paths) {
      result.push([start, ...path])
    }
  }

  return result
}

function sameArray(a, b) {
  if (a === b) return true
  if (a.length !== b.length) return false

  const N = a.length

  for (let i = 0; i < N; ++i) {
    if (a[i] instanceof Array) {
      if (!(b instanceof Array) || !sameArray(a[i], b[i])) return false
    } else if (a[i] !== b[i]) return false
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

    const isCorrect = sameArray(output, expected)

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

const t = new Tester(allPathsSourceTarget)

t.test(
  [
    [0, 1, 3],
    [0, 2, 3],
  ],
  [[1, 2], [3], [3], []]
)

t.test(
  [
    [0, 4],
    [0, 3, 4],
    [0, 1, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 4],
  ],
  [[4, 3, 1], [3, 2, 4], [3], [4], []]
)

t.report()
