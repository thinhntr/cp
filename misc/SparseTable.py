class SparseTable:
    """Minimum Sparse Table
    https://www.youtube.com/watch?v=uUatD9AudXo
    """

    def __init__(self, lst):
        ncol = len(lst)

        # Lookup table for floor(log2(i)), 1<=i<=N
        self.log2 = [0] * (ncol + 1)
        for i in range(2, ncol + 1):
            self.log2[i] = self.log2[i // 2] + 1

        # Number of rows in sparse table
        nrow = self.log2[ncol] + 1

        # Spare Table to find minimum values' index
        self.it = [[None] * ncol for _ in range(nrow)]
        self.it[0] = list(range(ncol))

        # Spare Table to find minimum values
        self.table = [[None] * ncol for _ in range(nrow)]
        self.table[0] = list(lst)

        # Fill the remaining rows
        for i in range(1, nrow):
            for j in range(ncol - (1 << i) + 1):
                left = self.table[i - 1][j]
                right = self.table[i - 1][j + (1 << (i - 1))]
                self.table[i][j] = min(left, right)

                self.it[i][j] = (
                    self.it[i - 1][i]
                    if left < right
                    else self.it[i - 1][j + (1 << (i - 1))]
                )

    def __getitem__(self, pos):
        return self.table[0][pos]

    def min(self, l, r):
        return self[self.argmin(l, r)]

    def argmin(self, l, r):
        row = self.log2[r - l + 1]
        left = self.it[row][l]
        right = self.it[row][r - (1 << row) + 1]
        return left if self[left] < self[right] else right
