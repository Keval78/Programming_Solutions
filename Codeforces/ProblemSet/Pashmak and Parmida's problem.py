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
from collections import Counter, defaultdict, deque
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
        self.seg_tree = [0]*(2*n)
        self.build()
    
    def build(self):
        for i in range(self.n-1, 0, -1):
            self.seg_tree[i] = self.seg_tree[i<<1] + self.seg_tree[i<<1|1]
    

    def update(self, i, val):
        i = i + self.n
        self.seg_tree[i] += val
        
        while i > 1:
            self.seg_tree[i>>1] = self.seg_tree[i] + self.seg_tree[i^1]
            i >>= 1
    
    def query(self, l, r):
        res = 0
        l, r = l + self.n, r + self.n
        while l < r:
            if l & 1:
                res += self.seg_tree[l]
                l += 1
            if r & 1:
                r -= 1
                res += self.seg_tree[r]
            l, r = l>>1, r>>1
        return res

    


def solve():
    n = ii()
    arr = li()

    fi = [0]*n
    fj = [0]*n

    freq = defaultdict(int)
    for i in range(n):
        freq[arr[i]] = freq.get(arr[i], 0) + 1
        fi[i] = freq[arr[i]]
    
    for i in range(n):
        fj[i] = freq[arr[i]]
        freq[arr[i]] -= 1

    # print(fi, fj)

    # Count smaller left in fi for each value of fj
    freq.clear()
    ind = 0
    for k in sorted(fi):
        if k not in freq:
            freq[k] = ind
            ind+=1

    ans = 0
    seg = SegmentTree(len(freq))
    for i in range(n):
        ans += seg.query(freq[fj[i]]+1, ind)
        seg.update(freq[fi[i]], 1)
    
    print(ans)

    


test = 1
# test = ii()
for _ in range(test):
    # print("case", _+1)
    solve()
