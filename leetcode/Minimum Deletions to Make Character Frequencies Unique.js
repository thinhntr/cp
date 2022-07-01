// https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
const _ = require('lodash')

function Counter(iterable) {
  const counter = new Map()
  _.forEach(iterable, (it) => counter.set(it, (counter.get(it) ?? 0) + 1))
  return counter
}

/**
 * @param {string} s
 * @return {number}
 */
var minDeletions = function (s) {
  const counts = [...Counter(s).values()]
  const countFreq = Counter(counts)
  let min = 0

  for (let [key, val] of countFreq.entries()) {
    while (val > 1) {
      let tmp = key
      while ((countFreq.get(tmp) ?? 0) > 0) {
        --tmp
        ++min
      }
      --val
      countFreq.set(key, val)
      if (tmp) countFreq.set(tmp, 1)
    }
  }

  return min
}

const test1 = minDeletions('aab') // 0
const test2 = minDeletions('aaabbbcc') // 2
const test3 = minDeletions('ceabaacb') // 2
const test4 = minDeletions('abcabc') // 3
const test5 = minDeletions('bbcebab') // 2
