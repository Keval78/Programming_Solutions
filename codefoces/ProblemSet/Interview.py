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
# from collections import Counter, defaultdict, deque
# from itertools import permutations, combinations
# from functools import reduce
# from heapq import heapify, heappop, heappush, heapreplace
# from bisect import bisect_left, bisect_right
# from operator import itemgetter


def si(): return sys.stdin.readline().strip()
def ii(): return int(si())
def mi(ss=" "): return map(int, si().split(ss))
def msi(ss=" "): return map(str, si().split(ss))
def li(ss=" "): return list(mi(ss))


sys.setrecursionlimit(10 ** 5)
MOD, MOD2, INF = 10 ** 9 + 7, 998244353, float('inf')
MAX = 10**5+1

# PYTHON Interactive code / Interactive problem...


# def input_str(left, right, pre):
#     ans = pre[right] - pre[left-1]
#     return ans
# ind = 7
# pre = [0 for i in range(n+1)]
# for i in range(n):
#     pre[i+1] = pre[i] + arr[i]
#     # print(i, ind)
#     if i == ind-1:
#         pre[i+1] += 1

for _ in range(ii()):
    n = ii()
    arr = li()

    prefix = [0 for i in range(n+1)]
    for i in range(n):
        prefix[i+1] = prefix[i] + arr[i]

    l, r = 1, n+1
    while l <= r:
        mid = (l+r)//2
        print("?", mid-l+1, *range(l, mid+1))
        sys.stdout.flush()
        input_s = ii()
        # print(input_str(l, mid, pre))
        if input_s <= prefix[mid]-prefix[l-1]:
            l = mid+1
        else:
            r = mid-1
    print("!", l)
    sys.stdout.flush()
