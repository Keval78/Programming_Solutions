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
from bisect import bisect, bisect_left, bisect_right
 
 
def si(): return sys.stdin.readline().strip()
def ii(): return int(si())
def mi(ss=" "): return map(int, si().split(ss))
def msi(ss=" "): return map(str, si().split(ss))
def li(ss=" "): return list(mi(ss))
 
 
sys.setrecursionlimit(10 ** 5)
MOD, MOD2, INF = 10 ** 9 + 7, 998244353, float('inf')
MAX = 10**5+1

def lcs(indices, i, j, l, r):
    if j==len(l): return True
    for digit in range(int(l[j]), int(r[j])+1):
        # print("----"*j + ">", digit, i)
        ind = bisect_left(indices[digit], i)
        if ind == len(indices[digit]): return False
        # print(indices[digit][ind])
        if not lcs(indices, indices[digit][ind]+1, j+1, l, r): return False
    return True

for _ in range(ii()):
    dbs = si()
    n = len(dbs)
    indices = [[] for i in range(10)] 
    for i in range(n):
        indices[int(dbs[i])].append(i)
    # print(indices)
    
    m = ii()
    l, r = si(), si()
    l, r = list(l), list(r)
    if lcs(indices, 0, 0, l, r):
        print("NO")
    else:
        print("YES")
