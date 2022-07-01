// https://leetcode.com/problems/valid-mountain-array/

/**
 * @param {number[]} arr
 * @return {boolean}
 */
var validMountainArray = function (arr) {
  const lastIdx = arr.length - 1
  if (arr.length < 3 || arr[0] >= arr[1] || arr[lastIdx - 1] <= arr[lastIdx])
    return false

  let isIncreasing = true

  for (let i = 1; i < lastIdx; ++i) {
    if (isIncreasing) {
      if (arr[i - 1] >= arr[i]) isIncreasing = false
    } else {
      if (arr[i - 1] <= arr[i]) return false
    }
  }

  return true
}

class Tester {
  constructor(fun) {
    this.fun = fun
    this.count = 0
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

const t = new Tester(validMountainArray)

t.test([0], false)
t.test([2, 1], false)
t.test([3, 5, 5], false)
t.test([3, 5, 2], true)
t.test([3, 1, 2], false)
t.test([0, 3, 2, 1], true)
t.test([1, 2, 3, 0], true)
t.test([1, 2, 3, 4, 5], false)
t.test([9, 8, 7, 6, 5], false)
t.test([0, 1, 2, 1, 2], false)

t.report()
