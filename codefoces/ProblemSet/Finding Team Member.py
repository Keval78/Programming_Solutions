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

n = ii()
teams = [0 for i in range(2*n)]
arr = []
for i in range(2*n-1):
    temp = li()
    for i in range(len(temp)):
        temp[i] = [temp[i], i+1]
    arr.append(sorted(temp, reverse=True))

# for a in arr:
#     print(a)

for i in range(n):
    curr_max, candidate1, candidate2 = 0, 0, 0
    for i in range(2*n-1):
        if teams[i+1] != 0: continue
        max_ind = -1
        for ind, val in enumerate(arr[i]):
            if teams[val[1]-1] == 0:
                max_ind = ind
                break
        if max_ind != -1 and curr_max < arr[i][max_ind][0]:
            curr_max, candidate1, candidate2 = arr[i][max_ind][0], i+2, arr[i][max_ind][1]
    #print(curr_max, candidate1, candidate2)
    teams[candidate1-1], teams[candidate2-1] = candidate2, candidate1
print(*teams)
    
