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

    odd, even = [], []
    for i in range(n):
        if arr[i] % 2:
            even.append(arr[i])
        else:
            odd.append(arr[i])

    odd.sort()
    even.sort()
    o, e = 0, 0
    for i in range(n):
        if arr[i] % 2:
            arr[i] = even[e]
            e += 1
        else:
            arr[i] = odd[o]
            o += 1

    for i in range(1, n):
        if arr[i] < arr[i-1]:
            print("NO")
            break
    else:
        print("YES")
