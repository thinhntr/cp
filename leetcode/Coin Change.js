// https://leetcode.com/problems/coin-change/

function coinChange(coins, amount) {
  const dp = new Array(amount + 1).fill(amount + 1);
  dp[0] = 0;
  for (const coin of coins) {
    for (let i = coin; i <= amount; ++i) {
      dp[i] = Math.min(dp[i], dp[i - coin] + 1);
    }
  }
  return dp[amount] != amount + 1 ? dp[amount] : -1;
}

let id = 1;

function test(coins, amount, expected) {
  const output = coinChange(coins, amount);
  const isCorrect = output === expected;
  console.log(`\nTest ${id++} ... ${isCorrect}`);
  if (!isCorrect) {
    console.log(`coins: ${coins}`);
    console.log(`amount: ${amount}`);
    console.error(`Output: ${output}`);
    console.error(`Expected: ${expected}`);
  }
}

test([1, 2, 5], 11, 3);
test([3], 3, 1);
test([2], 3, -1);
test([1], 0, 0);
test([186, 419, 83, 408], 6249, 20);
console.log("Finished.");
