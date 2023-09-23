'''
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

import math
import sys
# from os import path
# from math import log2, floor, ceil, sqrt, pow, gcd
# from random import random, randint, shuffle, choice
# from collections import Counter, defaultdict, deque
# from itertools import permutations, combinations
# from functools import reduce
# from heapq import heapify, heappop, heappush, heapreplace
# from bisect import bisect_left, bisect_right


def si(): return sys.stdin.readline().strip()
def ii(): return int(si())
def mi(ss=" "): return map(int, si().split(ss))
def msi(ss=" "): return map(str, si().split(ss))
def li(ss=" "): return list(mi(ss))


sys.setrecursionlimit(10 ** 5)
MOD, MOD2, INF = 10 ** 9 + 7, 998244353, float('inf')
MAX = 10**5+1

# Implementing Segment Tree...


class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.seg_tree = [0]*(self.n*2)
        self.build()

    def build(self):
        n = self.n
        for i in range(n-1, 0, -1):
            self.seg_tree[i]  # = self.seg_tree[i<<1], self.seg_tree[i<<1|1]

    def update(self, p):
        n = self.n
        self.seg_tree[p+n] = 1
        i = p+n
        while i > 1:
            self.seg_tree[i >> 1] = self.seg_tree[i] + self.seg_tree[i ^ 1]
            i >>= 1

    def query(self, l, r):
        res, n = 0, self.n
        l, r = l+n, r+n
        while l < r:
            if l & 1:
                res += self.seg_tree[l]
                l += 1
            if r & 1:
                r -= 1
                res += self.seg_tree[r]
            l, r = l >> 1, r >> 1
        return res


def solve():
    n = ii()
    arr = li()

    # Count greater left
    pairs = [0] * n

    indices = {}
    temp = list(arr)
    temp.sort(reverse=True)
    for i, num in enumerate(temp):
        indices[num] = i
    lseg = SegmentTree(n)
    for i in range(n):
        pairs[i] = lseg.query(0, indices[arr[i]])
        lseg.update(indices[arr[i]])

    # Count smaller right
    rseg = SegmentTree(n)
    for i in range(n-1, -1, -1):
        pairs[i] *= rseg.query(indices[arr[i]], n)
        rseg.update(indices[arr[i]])

    # for each element count greater left and smaller right
    ans = sum(pairs)
    print(ans)


test = 1
# test = ii()
for _ in range(test):
    # print("case", _+1)
    solve()
