// https://leetcode.com/problems/stone-game-iv/

const cache = { 0: false, 1: true, 2: false, 3: true, 4: true }

/**
 * @param {number} n
 * @return {boolean}
 */
function winnerSquareGame(n) {
  if (n in cache) return cache[n]

  let sqrt = Math.sqrt(n)
  if (sqrt === Math.floor(sqrt)) {
    cache[n] = true
    return true
  }
  sqrt = Math.floor(sqrt)

  for (let i = sqrt; i >= 1; --i) {
    if (winnerSquareGame(n - i * i)) continue
    cache[n] = true
    return true
  }

  cache[n] = false
  return false
}

class Tester {
  constructor(fun) {
    this.fun = fun
    this.count = 1
    this.fail = 0
    this.time = 0
  }

  test(input, expected) {
    const start = performance.now()
    const output = this.fun(input)
    this.time += performance.now() - start

    const isCorrect = output === expected

    console.log('Test', this.count, '...', isCorrect)

    if (!isCorrect) {
      console.error('Input:', input)
      console.error('Output:', output)
      console.error('Expected:', expected)
      this.fail += 1
    }

    console.log('')

    ++this.count
  }

  report() {
    console.log(`Ran in ${this.time}`)
    console.log(`Passed ${this.count - this.fail} / ${this.count} tests`)
  }
}

const t = new Tester(winnerSquareGame)

t.test(0, false)
t.test(1, true)
t.test(2, false)
t.test(3, true)
t.test(4, true)
t.test(5, false)
t.test(6, true)
t.test(7, false)
t.test(8, true)
t.test(9, true)
t.test(17, false)

t.report()
