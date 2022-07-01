// https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/

import Tester, { prettyPrint } from './tester.js'

var minimumTime = function (s) {
  if (!s.length) return 0

  const n = s.length
  const countFromLeft = [0]
  const countFromRight = [0]

  for (let i = 0; i < n; ++i) {
    if (s[i] !== '0') {
      countFromLeft.push(Math.min(countFromLeft.at(-1) + 2, i + 1))
    }

    if (s[n - i - 1] !== '0') {
      countFromRight.push(Math.min(countFromRight.at(-1) + 2, i + 1))
    }
  }

  const countN = countFromLeft.length

  if (!countN) return 0
  if (countN < 2) return Math.min(countFromLeft[0], countFromRight[0])

  let min = Math.min(countFromLeft.at(-1), countFromRight.at(-1))

  for (let i = 1; i < countN - 1; ++i) {
    min = Math.min(min, countFromLeft[i] + countFromRight[countN - i - 1])
  }

  return min
}

const t = new Tester(minimumTime)

t.test(5, '0100110')
t.test(5, '1100101')
t.test(2, '0010')
t.test(2, '0011')
t.test(0, '00000000')
t.test(0, '')
t.test(7, '01011010')
t.test(1, '000001')
t.test(1, '100000')
t.test(2, '100001')
t.test(1, '000000001')
t.test(1, '10000000')
t.test(2, '10000001')
t.test(40, '110001110000100001100010111101010011101101000111')

t.report()
