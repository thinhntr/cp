// https://leetcode.com/problems/gas-station/

/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
// var canCompleteCircuit = function (gas, cost) {
//   const startIdxs = Array.from(gas.keys()).filter(
//     (_, idx) => gas[idx] >= cost[idx]
//   )

//   if (!startIdxs.length) return -1

//   const n = gas.length

//   for (const startIdx of startIdxs) {
//     let i = 0
//     let remain = 0
//     for (; i < n; ++i) {
//       const curIdx = (startIdx + i) % n
//       remain += gas[curIdx] - cost[curIdx]
//       if (remain < 0) break
//     }
//     if (i === n) return startIdx
//   }

//   return -1
// }

var canCompleteCircuit = function (gas, cost) {
  const arr = Array.from(gas).map((it, idx) => it - cost[idx])

  if (arr.reduce((a, b) => a + b) < 0) return -1

  let total = 0
  let [bc_max, bg_max, e_max, cur_max, glo_max] = [0, 0, 0, 0, arr[0]]
  let [bc_min, bg_min, e_min, cur_min, glo_min] = [0, 0, 0, 0, arr[0]]

  arr.forEach((it, i) => {
    total += it

    // find max
    if (0 > cur_max) {
      cur_max = it
      bc_max = i
    } else {
      cur_max += it
    }
    
    if (cur_max > glo_max) {
      glo_max = cur_max
      bg_max = bc_max
      e_max = i
    }

    // find min
    if (0 < cur_min) {
      cur_min = it
      bc_min = i
    } else {
      cur_min += it
    }
    
    if (cur_min < glo_min) {
      glo_min = cur_min
      bg_min = bc_min
      e_min = i
    }
  })

  if (total !== glo_min && glo_max < total - glo_min) {
    return (e_min + 1) % gas.length
  }

  return bg_max
}

class Tester {
  constructor(fun) {
    this.fun = fun
    this.count = 0
    this.time = 0
  }

  test(gas, cost, expected) {
    const start = performance.now()
    const output = this.fun(gas, cost)
    this.time += performance.now() - start

    const isCorrect = output === expected

    console.log('Test', this.count, '...', isCorrect)

    if (!isCorrect) {
      console.error('Output:', output)
      console.error('Expected:', expected)
    }

    ++this.count
  }

  report() {
    console.log(`Ran ${this.count} tests in ${this.time}`)
  }
}

const t = new Tester(canCompleteCircuit)

t.test([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3)
t.test([2, 3, 4], [3, 4, 3], -1)
t.test([5, 1, 2, 3, 4], [4, 4, 1, 5, 1], 4)

t.report()

// [5, 1, 2, 3, 4]
// [4, 4, 1, 5, 1]
// [1,-1, 1,-2, 3]
