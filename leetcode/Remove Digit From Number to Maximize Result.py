# https://leetcode.com/contest/weekly-contest-291/problems/remove-digit-from-number-to-maximize-result/

from tester import Tester


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        digits = str(number)
        removed_index = 0
        for i in range(len(digits)):
            if digits[i] != digit:
                continue
            removed_index = i
            if i + 1 < len(digits) and digits[i] < digits[i  + 1]:
                break
        return digits[:removed_index] + digits[removed_index + 1:]


t = Tester(Solution())

t.test("13325", "133235","3")
t.test("12", "123", "3")
t.test("231", "1231", "1")
t.test("2513", "25153", "5")
t.test("25537", "255357", "5")

t.report()
