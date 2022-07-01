// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  const sells = prices.slice(0)

  for (let i = sells.length - 2; i >= 0; --i) {
    sells[i] = Math.max(sells[i], sells[i + 1])
  }

  let profit = 0

  for (let i = 0; i < prices.length; ++i) {
    profit = Math.max(profit, sells[i] - prices[i])
  }

  return profit
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

const t = new Tester(maxProfit)

t.test(5, [7, 1, 5, 3, 6, 4])
t.test(0, [7, 6, 4, 3, 1])
t.test(15, [7, 6, 5, 10, 9, 20])

t.report()
