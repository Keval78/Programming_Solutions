'''
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

# from os import path
# from math import log2, floor, ceil, sqrt, pow, gcd
# from random import random, randint, shuffle, choice
# from collections import Counter, defaultdict, deque
# from itertools import permutations, combinations
# from functools import reduce
# from heapq import heapify, heappop, heappush, heapreplace
# from bisect import bisect_left, bisect_right


import sys
def si(): return sys.stdin.readline().strip()
def ii(): return int(si())
def mi(ss=" "): return map(int, si().split(ss))
def msi(ss=" "): return map(str, si().split(ss))
def li(ss=" "): return list(mi(ss))


sys.setrecursionlimit(10 ** 5)
MOD, MOD2, INF = 10 ** 9 + 7, 998244353, float('inf')
MAX = 10**5+1


def solve():
    arr = []
    for i in range(10):
        arr.append(si())

    scores = [0]*6
    for i in range(10):
        for j in range(10):
            if i in [0, 9] or j in [0, 9]:
                if arr[i][j] == "X":
                    scores[1] += 1
            elif i in [1, 8] or j in [1, 8]:
                if arr[i][j] == "X":
                    scores[2] += 1
            elif i in [2, 7] or j in [2, 7]:
                if arr[i][j] == "X":
                    scores[3] += 1
            elif i in [3, 6] or j in [3, 6]:
                if arr[i][j] == "X":
                    scores[4] += 1
            elif i in [4, 5] or j in [4, 5]:
                if arr[i][j] == "X":
                    scores[5] += 1

    print(sum([i*s for i, s in enumerate(scores)]))


# test = 1
test = ii()
for _ in range(test):
    # print("case", _+1)
    solve()
