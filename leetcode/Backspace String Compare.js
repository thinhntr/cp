// https://leetcode.com/problems/backspace-string-compare/
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var backspaceCompare = function (s, t) {
  let [i, j] = [s.length - 1, t.length - 1]

  let sbs = 0
  let tbs = 0

  while (i >= 0 || j >= 0) {
    while (sbs && s[i] !== '#') {
      --i
      --sbs
    }

    while (tbs && t[j] !== '#') {
      --j
      --tbs
    }

    while (s[i] === '#') {
      ++sbs
      --i
    }

    if (sbs) continue

    while (t[j] === '#') {
      ++tbs
      --j
    }

    if (tbs) continue

    if (
      (i < 0 && j >= 0) ||
      (i >= 0 && j < 0) ||
      (i >= 0 && j >= 0 && s[i] !== t[j])
    ) {
      return false
    } else {
      --i
      --j
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

const t = new Tester(backspaceCompare)

t.test(true, 'ab#c', 'ad#c')
t.test(true, 'ab##', 'c#d#')
t.test(true, 'xywrrmp', 'xywrrmui##p')
t.test(true, 'xyw###', 'w#')
t.test(true, 'bxj##tw', 'bxo#j##tw')

t.report()
