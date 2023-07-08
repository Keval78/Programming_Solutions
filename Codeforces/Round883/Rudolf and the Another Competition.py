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


sys.setrecursionlimit(10 ** 5)
MOD, MOD2, INF = 10 ** 9 + 7, 998244353, float('inf')


for _ in range(ii()):
    n, m, h = mi()
    arr = [li() for i in range(n)]
    #print(arr)

    # sort every rows.
    for i in range(n):
        arr[i].sort()
    
    score = [(0,0,i+1) for i in range(n)]
    penalty = [[0 for i in range(m)] for j in range(n)]

    for i in range(n):
        for j in range(m):
            if j==0:
                penalty[i][j] = arr[i][j]
            else:
                arr[i][j] += arr[i][j-1]
                penalty[i][j] = arr[i][j] + penalty[i][j-1]
            if arr[i][j] <= h:
                score[i] = (-j-1, penalty[i][j], i+1)
    # print(arr)
    # print(penalty)
    # print(score)
    score.sort()
    #print(score)
    
    for i in range(n):
        if score[i][2] == 1:
            print(i+1)
            break
