'''
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

'''
Datastructures, Algorithms, Dynamic Programming, Introduction to Dynamic Programming 1, Bitmask
'''

import math
import sys
# from os import path
# from math import log2, floor, ceil, sqrt, pow, gcd
# from random import random, randint, shuffle, choice
# from collections import Counter, defaultdict, deque
from itertools import permutations, combinations
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

# Memorization
def optway(mask, rndnum, arr, dp):
    n = len(arr)
    k = n//2
    if rndnum > k: return 0
    if dp[rndnum][mask] != -1:
        return dp[rndnum][mask]
    
    maxi = -1
    for i in range(n):
        if (1<<i)&mask == 0:
            for j in range(i+1, n):
                if (1<<j)&mask == 0:
                    curr = rndnum * (arr[i]&arr[j])
                    new_mask = mask|(1<<i)|(1<<j)
                    maxi = max(maxi, curr + optway(new_mask, rndnum+1, arr, dp))
    
    dp[rndnum][mask] = maxi
    return dp[rndnum][mask]

def solve():
    n = ii()
    arr = li()
    k = ii()
    mask = (1<<n)-1
    # dp = [[0 for i in range(mask+1)] for j in range(k+1)]
    dp = [0 for i in range(mask+1)]


    # Tabulation
    bit_num = [[] for _ in range(n + 1)]
    for i in range(1 << n):
        bit_num[bin(i).count('1')].append(i)
    # print(bit_num)

    for rnd in range(1, k+1):
        for bit in bit_num[2*rnd]:
            for i in range(n):
                if (1<<i)&bit == 0: continue
                for j in range(i+1, n):
                    if (1<<j)&bit == 0: continue
                    score = rnd * (arr[i]&arr[j])
                    prev_mask = bit^(1<<i)^(1<<j)
                    dp[bit] = max(dp[bit], score + dp[prev_mask])
    
    print(dp[-1])

    # ans = optway(0, 1, arr, dp)
    # print(ans)


test = 1
# test = ii()
for _ in range(test):
    solve()

