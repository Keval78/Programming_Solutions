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


def si(): return sys.stdin.readline().strip()
def ii(): return int(si())
def mi(ss=" "): return map(int, si().split(ss))
def msi(ss=" "): return map(str, si().split(ss))
def li(ss=" "): return list(mi(ss))


sys.setrecursionlimit(10 ** 5)
MOD, MOD2, INF = 10 ** 9 + 7, 998244353, float('inf')
MAX = 10**5+1

n = ii()
arr = li()
brr = li()

ans = [0 for i in range(n)]
visit = [False for i in range(n)]
ind = []
for i in range(n):
    if arr[i] == brr[i]:
        ans[i] = arr[i]
        visit[arr[i]-1] = True
    else:
        ind.append(i)
if len(ind) == 1:
    ans[ind[0]] = n*(n+1)//2 - sum(ans)
else:
    if not visit[arr[ind[0]]-1] and not visit[brr[ind[1]]-1]:
        ans[ind[0]], ans[ind[1]] = arr[ind[0]], brr[ind[1]]
    else:
        ans[ind[0]], ans[ind[1]] = brr[ind[0]], arr[ind[1]]

print(*ans)

