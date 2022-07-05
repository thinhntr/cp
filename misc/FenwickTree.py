class FenwickTree:
    """https://cp-algorithms.com/data_structures/fenwick.html#definition-of-gi"""

    def __init__(self, A):
        self.n = len(A)
        self.bit = [0] * len(A)
        for i, item in enumerate(A):
            self.add(i, item)

    def sum(self, l, r=None):
        if r is not None:
            return self.sum(r) - self.sum(l - 1)
        res = 0
        while l >= 0:
            res += self.bit[l]
            l = (l & (l + 1)) - 1
        return res

    def add(self, idx, delta):
        while idx < self.n:
            self.bit[idx] += delta
            idx |= idx + 1


if __name__ == "__main__":
    a = Fenwick([1, 2, 3, 4, 5, 6, 7])
    print(a.sum(4, 5))
