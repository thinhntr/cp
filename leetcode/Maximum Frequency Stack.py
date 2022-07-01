# https://leetcode.com/problems/maximum-frequency-stack/
from collections import Counter
from heapq import heappush, heappop
from itertools import count
from icecream import ic


class FreqStack:
    """Implementation using priority queue"""
    def __init__(self):
        self.pq = []
        self.freq = {}
        self.idxs = count(0, -1)

    def push(self, val: int) -> None:
        idx = next(self.idxs)
        freq = self.freq[val] - 1 if val in self.freq else 0
        self.freq[val] = freq
        entry = (freq, idx, val)
        heappush(self.pq, entry)

    def pop(self) -> int:
        entry = heappop(self.pq)
        self.freq[entry[2]] += 1
        return entry[2]

class FreqStack:
    """Implementation using stack of stacks"""
    def __init__(self):
        self.stacks = []
        self.freq = Counter()

    def push(self, val: int) -> None:
        pos = self.freq[val]
        self.freq[val] += 1
        if pos < len(self.stacks):
            self.stacks[pos].append(val)
        else:
            self.stacks.append([val])
        

    def pop(self) -> int:
        val = self.stacks[-1].pop()
        self.freq[val] -= 1
        if not self.stacks[-1]:
            self.stacks.pop()
        return val


ops = [
    "push",
    "push",
    "push",
    "push",
    "pop",
    "pop",
    "push",
    "push",
    "push",
    "pop",
    "pop",
    "pop",
]
args = [[1], [1], [1], [2], [], [], [2], [2], [1], [], [], []]
obj = FreqStack()

for method, param in zip(ops, args):
    ic(method, param, getattr(obj, method)(*param))
    # if method == "pop":
    #     ic(obj.pq)
