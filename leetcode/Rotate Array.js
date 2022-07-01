// https://leetcode.com/problems/rotate-array/

function reverse(nums, start, end) {
  for (; start < end; ++start, --end) {
    const tmp = nums[start]
    nums[start] = nums[end]
    nums[end] = tmp
  }
}
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
// var rotate = function (nums, k) {
//   const N = nums.length
//   k = k % N
//   const tmp = Array(N)
//     .fill()
//     .map((_, idx) => nums[(idx + N - k) % N])
//   for (let i = 0; i < N; ++i) {
//     nums[i] = tmp[i]
//   }
// }

var rotate = function (nums, k) {
  k = k % nums.length
  reverse(nums, 0, nums.length - k - 1)
  reverse(nums, nums.length - k, nums.length - 1)
  reverse(nums, 0, nums.length - 1)
}

const something = [1, 2, 3, 4, 5, 6, 7]
rotate(something, 3)

console.log(something)
