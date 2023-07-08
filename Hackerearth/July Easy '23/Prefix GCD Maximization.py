'''
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
import sys
from os import path
from math import log2, floor, ceil, sqrt, pow, gcd
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

# Constants
sys.setrecursionlimit(10 ** 5)
MOD, MOD2, INF = 10 ** 9 + 7, 998244353, float('inf')

def gcd(a, b): return gcd(b, a%b) if b!=0 else a

n, arr = ii(), li()

two_n = (1<<n)
dp = [0 for i in range(two_n)]

for msk in range(two_n):
    g = 0
    for j in range(n):
        if (msk >> j) & 1 == 1:
            g = gcd(g, arr[j])
 
    for i in range(n):
        if (msk>>i)&1 == 0:
            dp[msk|(1<<i)] = max(dp[msk|(1<<i)], dp[msk] + gcd(arr[i], g))
print(dp[-1])
