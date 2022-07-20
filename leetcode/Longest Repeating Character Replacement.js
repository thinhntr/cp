// https://leetcode.com/problems/longest-repeating-character-replacement/

import _ from 'lodash';
import Tester from './tester.js';

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function (s, k) {
  const n = s.length;
  let res = 1;
  for (let len = n; len >= 2; len--) {
    for (let start = 0; start < n - len + 1; start++) {
      const counter = _(s)
        .slice(start, start + len)
        .countBy()
        .values()
        .value();
      if (len - Math.max(...counter) <= k) return len;
    }
  }
  return res;
};

const t = new Tester(characterReplacement);

t.test(4, 'AABABBA', 1);
t.test(
  7,
  'KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF',
  4
);
t.test(4, 'ABAB', 2);
t.test(4, 'AAAA', 2);

t.report();
