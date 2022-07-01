# https://leetcode.com/problems/find-median-from-data-stream/

from heapq import heappop, heappush


class MedianFinder:
    def __init__(self):
        self.left = []  # max heap
        self.right = []  # min heap

    def addNum(self, num: int) -> None:
        heappush(self.left, -num)

        if len(self.left) - len(self.right) > 1:
            maxleft = -heappop(self.left)
            heappush(self.right, maxleft)

        if len(self.right) - len(self.left) > 1:
            minright = heappop(self.right)
            heappush(self.left, -minright)

        if self.left and self.right and -self.left[0] > self.right[0]:
            maxleft = -heappop(self.left)
            minright = heappop(self.right)
            heappush(self.left, -minright)
            heappush(self.right, maxleft)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        if len(self.left) < len(self.right):
            return self.right[0]
        return (-self.left[0] + self.right[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(3)
obj.addNum(2)
obj.addNum(7)
obj.addNum(4)
print(obj.findMedian())
