export default class Tester {
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

const prettyPrint = (arr) => {
  const n = arr.length
  process.stdout.write(`(${n}) [`)
  for (const [i, it] of arr.entries()) {
    process.stdout.write(it < 10 ? ' ' : '')
    process.stdout.write(it.toString())
    process.stdout.write(i < n - 1 ? ' ' : '')
  }
  process.stdout.write(']\n')
}

const arange = (start, end) =>
  Array(end - start)
    .fill()
    .map((_, idx) => idx + start)

const swap = (arr, i, j) => {
  ;[arr[i], arr[j]] = [arr[j], arr[i]]
}

export { prettyPrint, arange, swap }
