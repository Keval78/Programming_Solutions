'''
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

import sys
# from os import path
from math import log2, floor, ceil, sqrt, pow, gcd
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


m, b = mi()

# x_bananas = []
# y_bananas = []
# for i in range(0, m*b+1):
#     y_lim = floor(b - i/m)
#     ans = (y_lim*(y_lim+1))//2 + (y_lim+1)*i
#     x_bananas.append(ans)

# for i in range(0, b+1):
#     x_lim = m*b-(b-i)*m
#     ans = (x_lim)*(x_lim+1)//2 + (x_lim+1)*(b-i)
#     y_bananas.append(ans)

# print(x_bananas)
# print(y_bananas)

max_totl, ans = 0, 0
for i in range(0, m*b+1):
    y_lim = floor(b - i/m)
    x_banana = (y_lim*(y_lim+1))//2 + (y_lim+1)*i
    # print(x_banana)
    ans += x_banana
    max_totl = max(max_totl, ans)
    if i % m == 0:
        x_lim = m*b-(b-i//m)*m
        y_banana = (x_lim)*(x_lim+1)//2 + (x_lim+1)*(b-i//m)
        # print(y_banana)
        ans -= y_banana
print(max_totl)
