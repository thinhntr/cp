// https://leetcode.com/problems/sequential-digits/

/**
 * @param {number} low
 * @param {number} high
 * @return {number[]}
 */
var sequentialDigits = function (low, high) {
  const [l_len, l_start] = analyze(low)
  const [h_len, h_start] = analyze(high)
  const result = []

  let tmp = l_start

  for (let l = l_len; l <= h_len; ++l) {
    for (let s = tmp; s <= 10 - l; ++s) {
      const num = generateNum(s, l)
      if (num < low) continue
      if (num > high) break

      result.push(num)
    }
    tmp = 1
  }

  return result
}

function analyze(num) {
  let n = num
  let len = 0
  let ten = 1
  while (num) {
    ++len
    ten *= 10
    num = Math.floor(num / 10)
  }
  return [len, Math.floor((n / ten) * 10)]
}

function generateNum(start, length) {
  let num = 0
  for (let l = 0; l < length; ++l) {
    num = num * 10 + start + l
  }
  return num
}

function cmpArray(arr1, arr2) {
  if (arr1 === arr2) return true

  if (arr1.length !== arr2.length) return false

  for (let i = 0; i < arr1.length; ++i) if (arr1[i] !== arr2[i]) return false

  return true
}

class Tester {
  constructor(fun) {
    this.fun = fun
    this.count = 0
    this.fail = 0
    this.time = 0
  }

  test(low, high, expected) {
    const start = performance.now()
    const output = this.fun(low, high)
    this.time += performance.now() - start

    const isCorrect = cmpArray(output, expected)

    console.log('Test', this.count, '...', isCorrect)

    if (!isCorrect) {
      console.error('Output:', output)
      console.error('Expected:', expected)
      ++this.fail
    }

    console.log('')
    ++this.count
  }

  report() {
    console.log(`Passed ${this.count - this.fail} tests`)
    console.log(`Ran ${this.count} tests in ${this.time}`)
  }
}

const t = new Tester(sequentialDigits)

t.test(200, 300, [234])
t.test(200, 222, [])
t.test(100, 300, [123, 234])
t.test(1000, 13000, [1234, 2345, 3456, 4567, 5678, 6789, 12345])
t.test(58, 155, [67, 78, 89, 123])

t.report()
