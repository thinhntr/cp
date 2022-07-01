// https://leetcode.com/problems/design-bitset/

/**
 * @param {number} size
 */
class Bitset {
  constructor(size) {
    this.size = size
    this.ones = new Set()
    this.zeros = new Set()

    for (let i = 0; i < size; ++i) this.zeros.add(i)
  }

  fix(idx) {
    this.ones.add(idx)
    this.zeros.delete(idx)
  }

  unfix(idx) {
    this.ones.delete(idx)
    this.zeros.add(idx)
  }

  flip() {
    ;[this.ones, this.zeros] = [this.zeros, this.ones]
  }

  all() {
    return this.ones.size === this.size
  }

  one() {
    return this.ones.size
  }

  count() {
    return this.ones.size
  }

  toString() {
    const tmp = Array(this.size).fill(0)
    for (const oneIdx of this.ones) tmp[oneIdx] = 1
    return tmp.join('')
  }
}

/**
 * Your Bitset object will be instantiated and called as such:
 * var obj = new Bitset(size)
 * obj.fix(idx)
 * obj.unfix(idx)
 * obj.flip()
 * var param_4 = obj.all()
 * var param_5 = obj.one()
 * var param_6 = obj.count()
 * var param_7 = obj.toString()
 */
