// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

function swap(nums, i, j) {
  const tmp = nums[i]
  nums[i] = nums[j]
  nums[j] = tmp
}

/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
  let k = 1
  let prevCount = 1

  for (let i = 1; i < nums.length; ++i) {
    if (nums[i] !== nums[k - 1]) {
      swap(nums, i, k)
      prevCount = 1
      ++k
    } else if (prevCount < 2) {
      swap(i, k)
      ++k
      ++prevCount
    }
  }

  return k
}
