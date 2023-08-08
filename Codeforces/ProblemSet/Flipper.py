'''
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

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


# sys.setrecursionlimit(10 ** 5)
MOD, MOD2, INF = 10 ** 9 + 7, 998244353, float('inf')
MAX = 10**5+1

for _ in range(ii()):
    n = ii()
    arr = li()

    if n==1:
        print(*arr)
        continue
    # print(arr)
    start = arr.index(n)
    if start==0:
        start = arr.index(n-1)
    
    max_arr = [0]*n
    if start == n-1:
        l = start
        while start==l or arr[l] > arr[0]:
            l-=1
        max_arr = arr[start:l:-1] + arr[:l+1]
    else:
        for l in range(start):
            if l==0:
                curr = arr[start:] + arr[start-1::-1]
            else:
                curr = arr[start:] + arr[start-1:l-1:-1] + arr[:l]
            max_arr = max(max_arr, curr)
    print(*max_arr)

