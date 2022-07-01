var isNStraightHand = function (hand, groupSize) {
  const n = hand.length
  if (n % groupSize) return false

  const counter = new Map()
  for (let item of hand) {
    const val = counter.get(item) ? counter.get(item) : 0
    counter.set(item, val + 1)
  }

  const keys = [...counter.keys()].sort((a, b) => a - b)
  let minKeyIdx = 0
  const numGroup = Math.floor(n / groupSize)

  for (let i = 0; i < numGroup; i++) {
    while (minKeyIdx < keys.length && !counter.get(keys[minKeyIdx])) {
      minKeyIdx++
    }
    if (minKeyIdx >= keys.length) {
      return false
    }
    let key = keys[minKeyIdx]
    for (let i = 0; i < groupSize; i++) {
      if (!counter.get(key + i)) {
        return false
      }
      counter.set(key + i, counter.get(key + i) - 1)
    }
  }

  return true
}

console.log(isNStraightHand([8, 8, 9, 7, 7, 7, 6, 7, 10, 6], 2) === true)
console.log(isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3) === true)
console.log(isNStraightHand([8, 10, 12], 3) === false)
console.log(isNStraightHand([1, 2, 3, 4, 5], 4) === false)
