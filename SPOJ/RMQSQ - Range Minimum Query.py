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


# sys.setrecursionlimit(10 ** 5)
MOD, MOD2, INF = 10 ** 9 + 7, 998244353, float('inf')
MAX = 10**5+1


class SparseTable:
    def __init__(self):
        self.sp_table = []
        self.K = 0
        self.LIMIT = 10**9
        self.bin_log = [0 for i in range(MAX)]

    def build(self, arr, n):
        self.K = int(math.log2(n) + 1)
        # print(self.K)
        self.bin_log[1] = 0
        for i in range(2, n+1):
            self.bin_log[i] = self.bin_log[i//2]+1
        self.sp_table = [[0 for _ in range(n)] for _ in range(self.K)]

        for i in range(n):
            self.sp_table[0][i] = arr[i]

        for i in range(1, self.K):
            for j in range(n - (1 << i) + 1):
                self.sp_table[i][j] = min(
                    self.sp_table[i-1][j],
                    self.sp_table[i-1][j + (1 << (i-1))],
                )

        # for i in self.sp_table:
        #     print(i)

    def getmin(self, L, R):
        length = R-L+1
        k = self.bin_log[length]
        # print(k, L, R-(1<<k)+1)#, self.sp_table[k][L], self.sp_table[k][R-(1<<k)+1])
        print(min(self.sp_table[k][L], self.sp_table[k][R-(1 << k)+1]))


n = ii()
arr = li()
s = SparseTable()
s.build(arr, n)
q = ii()
for _ in range(q):
    L, R = mi()
    # print(arr[L], arr[R])
    s.getmin(L, R)
