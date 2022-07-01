// https://leetcode.com/problems/first-missing-positive/

import Tester from './tester.js'

/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function (nums) {
  const N = nums.length
  let num = 0
  let i = 0

  for (; i < N; ++i) {
    num = nums[i]

    while (0 < num && num < N && nums[num - 1] !== num) {
      // swap(nums, num - 1, i)
      nums[i] = nums[num - 1]
      nums[num - 1] = num
      num = nums[i]
    }
  }

  for (i = 0; i < N; ++i) {
    if (i + 1 !== nums[i]) return i + 1
  }

  return i + 1
}

const t = new Tester(firstMissingPositive)

t.test(2, [1])
t.test(3, [1, 2, 0])
t.test(1, [2147483647])
t.test(2, [3, 4, -1, 1])
t.test(6, [3, 2, 1, 4, 5])
t.test(1, [7, 8, 9, 11, 12])
t.test(6, [2, 7, 0, 3, 4, 5, 1, 8])
t.test(2, [3, 8, 0, 3, 4, 5, 1, 8])

t.report()

// [3, 8, 0, 3, 4, 5, 1, 8]
// [0, 8, 3, 3, 4, 5, 1, 8]
// [1, 8, 3, 4, 5, 3, 0, 8]
