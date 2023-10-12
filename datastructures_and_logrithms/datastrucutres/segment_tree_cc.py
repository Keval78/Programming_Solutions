"""
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/

Reference:
https://github.com/TheAlgorithms/Python/blob/master/data_structures/binary_tree/segment_tree.py



Segment Tree Easy & Fast Iplementation for Competitive Coding.
"""

# Implementing Segment Tree...
# Link: https://codeforces.com/blog/entry/18051


class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.seg_tree = [0]*self.n + arr
        self.build()

    def build(self):
        n = self.n
        for i in range(n-1, 0, -1):
            self.seg_tree[i] = self.seg_tree[i << 1] + \
                self.seg_tree[i << 1 | 1]

    def update(self, p, val):
        n = self.n
        self.seg_tree[p+n] = val
        i = p+n
        while i > 1:
            self.seg_tree[i >> 1] = self.seg_tree[i] + self.seg_tree[i ^ 1]
            i >>= 1

    def query(self, l, r):
        res, n = 0, self.n
        l, r = l+n, r+n
        print(self.seg_tree[l:r])
        while l < r:
            print(l, r)
            if l & 1:
                res += self.seg_tree[l]
                l += 1
            if r & 1:
                r -= 1
                res += self.seg_tree[r]
            l, r = l >> 1, r >> 1
        return res

    # def update(self, l, r, val):
    #     n = self.n
    #     l, r = l+n, r+n
    #     self.push_down(l, r)

    #     while l < r:
    #         if l & 1:
    #             self.seg_tree[l] += val
    #             l += 1
    #         if r & 1:
    #             r -= 1
    #             self.seg_tree[r] += val
    #         l, r = l >> 1, r >> 1

    #     self.push_up(l, r)

    # def push_down(self, l, r):
    #     if self.lazy[l] != 0:
    #         self.seg_tree[l] += self.lazy[l] * (r-l)
    #         if l < r-1:
    #             self.lazy[l << 1] += self.lazy[l]
    #             self.lazy[l << 1 | 1] += self.lazy[l]
    #         self.lazy[l] = 0

    # def push_up(self, l, r):
    #     while l > 1:
    #         self.seg_tree[l >> 1] = self.seg_tree[l] + self.seg_tree[l ^ 1]
    #         l >>= 1


arr = [1, 2, 3, 4, 5, 6, 7, 8]
segt = SegmentTree(arr)
print(segt.seg_tree)
print(segt.query(1, 3))
segt.update(2, 1)
print(segt.seg_tree)
print(segt.query(1, 3))
print(segt.query(2, 7))
