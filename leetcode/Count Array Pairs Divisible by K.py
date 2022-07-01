# https://leetcode.com/problems/count-array-pairs-divisible-by-k/
import math
from collections import defaultdict
from typing import List
from tester import Tester

import math


class Solution:
    def coutPairs(self, nums: List[int], k: int) -> int:
        factors = defaultdict(int)
        for i in range(1, int(math.sqrt(k)) + 1):
            if k % i == 0:
                factors[i] = 0
                if k // i != i:
                    factors[k//i] = 0

        result = 0

        for num in nums:
            gcd = math.gcd(num, k)
            for factor, count in factors.items():
                result += 0 if gcd * factor % k else count
                if gcd == factor:
                    factors[gcd]+=1
        return result


t = Tester(Solution())

t.test(1, [27, 8], 12)
t.test(7, [1, 2, 3, 4, 5], 2)
t.test(0, [1, 2, 3, 4], 5)
t.test(18, [8, 10, 2, 5, 9, 6, 3, 8, 2], 6)


t.report()
