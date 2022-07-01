# https://leetcode.com/contest/weekly-contest-287/problems/minimum-number-of-operations-to-convert-time/
from typing import List
from tester import Tester


class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        fh, fm = map(int, current.split(":"))
        ch, cm = map(int, correct.split(":"))
        count = 0
        fm += fh * 60
        cm += ch * 60
        m = cm - fm
        if m >= 60:
            count += m // 60
            m %= 60
        if m >= 15:
            count += m // 15
            m %= 15
        if m >= 5:
            count += m // 5
            m %= 5
        count += m
        return count


t = Tester(Solution())

t.test(7, "09:41", "10:34")
t.test(3, current="02:30", correct="04:35")
t.test(1, current="11:00", correct="11:01")

t.report()
