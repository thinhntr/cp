// https://leetcode.com/problems/richest-customer-wealth/

/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function (accounts) {
  return accounts.reduce(
    (maxWealth, account) =>
      Math.max(
        maxWealth,
        account.reduce((a, b) => a + b)
      ),
    0
  )
}
