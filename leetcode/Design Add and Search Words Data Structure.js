// https://leetcode.com/problems/design-add-and-search-words-data-structure/

class WordDictionary {
  constructor(root = null) {
    this.root = root ? root : new Map()
    this.isLeaf = false
  }

  /**
   * @param {string} word
   * @return {void}
   */
  addWord(word) {
    let curr = this

    for (const c of word) {
      if (!curr.root.has(c)) curr.root.set(c, new WordDictionary())
      curr = curr.root.get(c)
    }

    curr.isLeaf = true
  }

  /**
   * @param {string} word
   * @return {boolean}
   */
  search(word) {
    if (!word) return this.isLeaf

    const c = word[0]

    if (c !== '.') {
      if (this.root.has(c)) {
        const wd = this.root.get(c)
        if (wd.search(word.slice(1))) return true
      }
    } else {
      for (const root of this.root.values()) {
        if (root.search(word.slice(1))) return true
      }
    }
    return false
  }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * var obj = new WordDictionary()
 * obj.addWord(word)
 * var param_2 = obj.search(word)
 */

function test(ops, args, expected) {
  if (
    ops.length !== args.length ||
    ops.length !== expected.length ||
    args.length !== expected.length
  ) {
    console.error('Something went wrong')
    console.error('ops.length', ops.length)
    console.error('args.length', args.length)
    console.error('expected.length', expected.length)
    return
  }
  const wd = new WordDictionary()
  for (let i = 0; i < ops.length; ++i) {
    let output = null

    if (ops[i] !== 'search') {
      wd.addWord(args[i][0])
    } else {
      output = wd.search(args[i][0])
    }

    const passed = output === expected[i]
    console.log('Input:', args[i][0], '...', passed)

    if (!passed) {
      console.error('Output:', output)
      console.error('Expected:', expected[i])
    }

    console.log('')
  }
}

let ops = [
  'addWord',
  'addWord',
  'addWord',
  'search',
  'search',
  'search',
  'search',
]
let args = [['bad'], ['dad'], ['mad'], ['pad'], ['bad'], ['.ad'], ['b..']]
let expected = [null, null, null, false, true, true, true]
test(ops, args, expected)

ops = [
  'addWord',
  'addWord',
  'addWord',
  'addWord',
  'search',
  'search',
  'addWord',
  'search',
  'search',
  'search',
  'search',
  'search',
  'search',
]
args = [
  ['at'],
  ['and'],
  ['an'],
  ['add'],
  ['a'],
  ['.at'],
  ['bat'],
  ['.at'],
  ['an.'],
  ['a.d.'],
  ['b.'],
  ['a.d'],
  ['.'],
]
expected = [
  null,
  null,
  null,
  null,
  false,
  false,
  null,
  true,
  true,
  false,
  false,
  true,
  false,
]
test(ops, args, expected)

ops = [
  'addWord',
  'addWord',
  'search',
  'search',
  'search',
  'search',
  'search',
  'search',
  'search',
  'search',
]
args = [
  ['a'],
  ['ab'],
  ['a'],
  ['a.'],
  ['ab'],
  ['.a'],
  ['.b'],
  ['ab.'],
  ['.'],
  ['..'],
]
expected = [null, null, true, true, true, false, true, false, true, true]
test(ops, args, expected)
