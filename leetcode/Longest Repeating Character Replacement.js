// https://leetcode.com/problems/longest-repeating-character-replacement/

import _ from 'lodash';
import Tester from './tester.js';

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
const characterReplacement = function (s, k) {
	const counter = new Map([[s[0], 1]]);
	const n = s.length;
	let l = 0;
	let max_len = 1;
	let max_freq = 1;
	for (const r of _.range(1, n)) {
		counter.set(s[r], (counter.get(s[r]) ?? 0) + 1);
		max_freq = Math.max(max_freq, counter.get(s[r]));
		while (r - l + 1 - max_freq > k) {
			counter.set(s[l], counter.get(s[l]) - 1);
			l += 1;
		}
		max_len = Math.max(max_len, r - l + 1);
	}
	return max_len;
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
