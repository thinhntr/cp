// https://leetcode.com/problems/add-digits/

/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function (num) {
  if (num < 1) return 0
  return ((num - 1) % 9) + 1
}

// https://en.wikipedia.org/wiki/Digital_root#Congruence_formula
