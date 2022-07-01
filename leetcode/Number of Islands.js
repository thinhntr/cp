// https://leetcode.com/problems/number-of-islands/

/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function (grid) {
  const [nrow, ncol] = [grid.length, grid[0].length]
  const idToCell = {}
  const cellToId = Array(nrow)
    .fill()
    .map(() => Array(ncol).fill(null))

  let count = 0

  for (let r = 0; r < nrow; ++r) {
    for (let c = 0; c < ncol; ++c) {
      if (grid[r][c] === '0') continue

      const cell = r * ncol + c
      const aboveCellId = r < 1 ? null : cellToId[r - 1][c]
      const leftCellId = c < 1 ? null : cellToId[r][c - 1]

      if (aboveCellId && leftCellId) {
        cellToId[r][c] = aboveCellId
        idToCell[aboveCellId].push(cell)

        if (leftCellId !== aboveCellId) {
          for (const oldCell of idToCell[leftCellId]) {
            const oldR = Math.floor(oldCell / ncol)
            const oldC = oldCell % ncol

            cellToId[oldR][oldC] = aboveCellId
            idToCell[aboveCellId].push(oldCell)
          }

          delete idToCell[leftCellId]
        }
      } else if (!aboveCellId && !leftCellId) {
        ++count
        cellToId[r][c] = count
        idToCell[count] = [cell]
      } else {
        const finalId = aboveCellId ? aboveCellId : leftCellId
        cellToId[r][c] = finalId
        idToCell[finalId].push(cell)
      }
    }
  }

  return Object.keys(idToCell).length
}

class Tester {
  constructor(fun) {
    this.fun = fun
    this.total = 0
    this.fail = 0
    this.time = 0
  }

  get pass() {
    return this.total - this.fail
  }

  test(expected, ...input) {
    const start = performance.now()
    const output = this.fun(...input)
    this.time += performance.now() - start

    const isCorrect = output === expected

    console.log('Test', this.total, '...', isCorrect)

    if (!isCorrect) {
      console.error('Output:', output)
      console.error('Expected:', expected)
      ++this.fail
    }

    console.log('')
    ++this.total
  }

  report() {
    console.log(`Passed ${this.pass} / ${this.total} tests
`)
    console.log(`Ran in ${this.time.toFixed(4)}ms`)
  }
}

const t = new Tester(numIslands)

t.test(1, [
  ['1', '1', '1', '1', '0'],
  ['1', '1', '0', '1', '0'],
  ['1', '1', '0', '0', '0'],
  ['0', '0', '0', '0', '0'],
])

t.test(3, [
  ['1', '1', '0', '0', '0'],
  ['1', '1', '0', '0', '0'],
  ['0', '0', '1', '0', '0'],
  ['0', '0', '0', '1', '1'],
])

t.test(2, [
  ['1', '1', '1', '1', '1', '0', '1', '1', '1', '1'],
  ['1', '0', '1', '0', '1', '1', '1', '1', '1', '1'],
  ['0', '1', '1', '1', '0', '1', '1', '1', '1', '1'],
  ['1', '1', '0', '1', '1', '0', '0', '0', '0', '1'],
  ['1', '0', '1', '0', '1', '0', '0', '1', '0', '1'],
  ['1', '0', '0', '1', '1', '1', '0', '1', '0', '0'],
  ['0', '0', '1', '0', '0', '1', '1', '1', '1', '0'],
  ['1', '0', '1', '1', '1', '0', '0', '1', '1', '1'],
  ['1', '1', '1', '1', '1', '1', '1', '1', '0', '1'],
  ['1', '0', '1', '1', '1', '1', '1', '1', '1', '0'],
])

t.report()
