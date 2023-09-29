'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List


class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.seg_tree = [(0, 1)]*(self.n*2)
        self.build()

    def calculate(self, left, right):
        m = max(left[0], right[0])
        if m == 0:
            return (0, 1)
        if m == left[0] == right[0]:
            return (m, left[1] + right[1])
        elif m == left[0]:
            return (m, left[1])
        else:
            return (m, right[1])

    def build(self):
        for i in range(self.n-1, 0, -1):
            self.seg_tree[i] = self.calculate(
                self.seg_tree[i << 1], self.seg_tree[i << 1 | 1])

    def update(self, i, val):
        i = i + self.n
        self.seg_tree[i] = val
        while i > 1:
            self.seg_tree[i >> 1] = self.calculate(
                self.seg_tree[i], self.seg_tree[i ^ 1])
            i >>= 1

    def query(self, l, r):
        maxi, summ = 0, 0
        l, r = l+self.n, r+self.n

        while l < r:
            if l & 1:
                maxi = max(maxi, self.seg_tree[l][0])
                if maxi != 0 and maxi == self.seg_tree[l][0]:
                    summ += self.seg_tree[l][1]
                else:
                    summ = 0
                l += 1
            if r & 1:
                r -= 1
                maxi = max(maxi, self.seg_tree[r][0])
                if maxi != 0 and maxi == self.seg_tree[r][0]:
                    summ += self.seg_tree[r][1]
                else:
                    summ = 0
            l, r = l >> 1, r >> 1
        return (maxi, max(summ, 1))


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        indices = {}
        idx = 0
        for num in sorted(nums):
            if num in indices:
                continue
            indices[num] = idx
            idx += 1

        segt = SegmentTree(idx)
        # print(indices)
        n = len(nums)
        for i in range(n):
            # print(nums[i])
            (m, s) = segt.query(0, indices[nums[i]])
            # print(m, s)
            segt.update(indices[nums[i]], (m+1, s))

        (m, s) = segt.query(0, idx)
        print(m, s)
        return m


nums = [0, 1, 0, 3, 2, 3]
Solution().lengthOfLIS(nums)

nums = [7, 7, 7, 7, 7, 7, 7]
Solution().lengthOfLIS(nums)
