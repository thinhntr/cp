// https://leetcode.com/problems/k-diff-pairs-in-an-array/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findPairs = function (nums, k) {
  const map = new Map()

  nums.forEach((it) => map.set(it, (map.get(it) ?? 0) + 1))

  let count = 0

  for (const [key, val] of map) {
    if (!k) {
      if (val > 1) ++count
    } else {
      if (map.has(key + k)) ++count
    }
  }

  return count
}

console.log(findPairs([3, 1, 1, 5], 2)) // 2
console.log(findPairs([3, 1, 1, 3], 2)) // 1
console.log(findPairs([1, 2, 3, 4, 5], 1)) // 4
console.log(findPairs([3, 1, 4, 1, 5], 1)) // 2
console.log(findPairs([1, 3, 1, 5, 4], 0)) // 1
console.log(findPairs([6, 8, 5, 0, 5, 0, 3, 5, 9], 3)) // 4
console.log(findPairs([0, 0, 3], 3)) // 1
console.log(findPairs([2, 8, 6, 9, 7, 4, 9, 0, 5, 4], 1)) // 5
console.log(findPairs([4, 9, 3, 5, 3, 3, 9, 0], 0)) // 2
