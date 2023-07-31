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
from bisect import bisect_left, bisect_right


def si(): return sys.stdin.readline().strip()
def ii(): return int(si())
def mi(ss=" "): return map(int, si().split(ss))
def msi(ss=" "): return map(str, si().split(ss))
def li(ss=" "): return list(mi(ss))


sys.setrecursionlimit(10 ** 5)
MOD, MOD2, INF = 10 ** 9 + 7, 998244353, float('inf')
MAX = 10**5+1

for _ in range(ii()):
    n = ii()
    arr = li()

    dp = [arr[i] for i in range(n)]
    for i in range(n):
        if i>=2:
            dp[i] = max(dp[i], dp[i-2] + max(0,arr[i]))
    print(max(dp))

    # max_neg = max(arr)
    # odd_sum = even_sum = 0
    # for i in range(n):
    #     if arr[i]<=0: continue
    #     if i%2:
    #         odd_sum += arr[i]
    #     else:
    #         even_sum += arr[i]
    # print(max(max_neg, odd_sum if odd_sum>0 else -INF, even_sum if even_sum>0 else -INF))


