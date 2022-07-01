from collections import deque


class MaxQueue:
    @property
    def is_empty(self):
        return not len(self.q)

    def __init__(self):
        self.q = deque()
        self.cnt_added = 0
        self.cnt_removed = 0

    @property
    def max(self):
        return self.first

    @property
    def first(self):
        return self.q[0][0]

    @property
    def last(self):
        return self.q[-1][0]

    def append(self, new_element):
        while not self.is_empty and self.last < new_element:
            self.q.pop()
        self.q.append((new_element, self.cnt_added))
        self.cnt_added += 1

    def popleft(self):
        if (not self.is_empty and self.q[0][1] == self.cnt_removed):
            self.q.popleft()
        self.cnt_removed += 1


class MinQueue:
    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()

    @property
    def min(self):
        if not self.s1 or not self.s2:
            return self.s2[-1][1] if not self.s1 else self.s1[-1][1]
        else:
            return min(self.s1[-1][1], self.s2[-1][1])

    def append(self, value):
        minimum = value if not self.s1 else min(value, self.s1[-1][1])
        self.s1.append((value, minimum))

    def pop(self):
        if not self.s2:
            while self.s1:
                element = self.s1[-1][0]
                self.s1.pop()
                minimum = element if not self.s2 else min(element, self.s2[-1][1])
                self.s2.append((element, minimum))
        remove_element = self.s2[-1][0]
        self.s2.pop()
        return remove_element
