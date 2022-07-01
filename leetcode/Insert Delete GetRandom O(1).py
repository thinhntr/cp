from icecream import ic
from random import choice


class RandomizedSet:
    def __init__(self):
        self.array = []
        self.hashmap = {}

    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        self.hashmap[val] = len(self.array)
        self.array.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        idx = self.hashmap[val]
        self.array[idx], self.array[-1] = self.array[-1], self.array[idx]
        self.hashmap[self.array[idx]] = idx
        self.array.pop()
        del self.hashmap[val]
        return True

    def getRandom(self) -> int:
        return choice(self.array)


rds = RandomizedSet()
ic(rds.remove(0) == False)
ic(rds.remove(0) == False)
ic(rds.insert(0) == True)
ic(rds.getRandom() == 0)
ic(rds.remove(0) == True)
ic(rds.insert(0) == True)

print()

rds = RandomizedSet()
ic(rds.insert(1) == True)
ic(rds.insert(2) == True)
ic(rds.remove(1) == True)
ic(rds.getRandom() == 2)

print()

ops = ["insert","remove","insert","remove","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom"]
args = [[0],[0],[-1],[0],[],[],[],[],[],[],[],[],[],[]]

rds = RandomizedSet()
for op, arg in zip(ops, args):
    out = getattr(rds, op)(*arg)
    ic(op, *arg, out)