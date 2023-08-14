class Solution:
    def countSmaller(self, nums):
        def msort(idxs):
            half = len(idxs) // 2
            if not half:
                return idxs
            left, right = msort(idxs[:half]), msort(idxs[half:])
            for i in list(range(len(idxs) - 1, -1, -1)):
                if not right or left and nums[left[-1]] > nums[right[-1]]:
                    smaller[left[-1]] += len(right)
                    idxs[i] = left.pop()
                else:
                    idxs[i] = right.pop()
            return idxs
        smaller = [0] * len(nums)
        msort(list(range(len(nums))))
        return smaller
