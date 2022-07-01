// https://leetcode.com/problems/find-all-anagrams-in-a-string/

/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
var findAnagrams = function (s, p) {
  if (s.length < p.length) return []

  const pCounter = new Map()

  for (const c of p) {
    if (pCounter.has(c)) {
      pCounter.set(c, pCounter.get(c) + 1)
    } else {
      pCounter.set(c, 1)
    }
  }

  const result = []
  const sCounter = new Map()
  let total = 0

  for (let i = 0; i < s.length; ++i) {
    const c = s[i]

    if (i >= p.length) {
      const firstChar = s[i - p.length]
      if (sCounter.has(firstChar) && sCounter.get(firstChar) > 0) {
        sCounter.set(firstChar, sCounter.get(firstChar) - 1)
        if (sCounter.get(firstChar) < pCounter.get(firstChar)) --total
      }
    }

    if (pCounter.has(c)) {
      if (sCounter.has(c)) {
        sCounter.set(c, sCounter.get(c) + 1)
      } else {
        sCounter.set(c, 1)
      }

      if (sCounter.get(c) <= pCounter.get(c)) ++total
    }

    if (total === p.length) {
      result.push(i - p.length + 1)
    }
  }

  return result
}

function compareArray(a, b) {
  if (a === b) return true
  if (a.length !== b.length) return false

  for (const [idx, val] of a.entries()) {
    if (val !== b[idx]) return false
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

const t = new Tester(findAnagrams)

t.test([0, 6], 'cbaebabacd', 'abc')
t.test([0, 1, 2], 'abab', 'ab')
t.test([], 'bbb', 'ab')

t.report()
