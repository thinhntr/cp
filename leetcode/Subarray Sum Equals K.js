// https://leetcode.com/problems/subarray-sum-equals-k/

import Tester from './tester.js'

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function (nums, k) {
  let sum = 0
  let count = 0
  const counters = new Map()
  counters.set(0, 1)

  for (const num of nums) {
    sum += num
    count += counters.get(sum - k) ?? 0
    counters.set(sum, (counters.get(sum) ?? 0) + 1)
  }

  return count
}

const t = new Tester(subarraySum)

t.test(2, [1, 1, 1], 2)
t.test(2, [1, 2, 3], 3)
t.test(4, [1, 2, 0, 3], 3)
t.test(4, [0, 0, -1, 0], 0)
t.test(4, [0, 0, 1, 0], 0)
t.test(6, [0, -1, 1, 0], 0)
t.test(4, [0, 1, 2, 0], 3)

t.report()
