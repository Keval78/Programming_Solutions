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
        if i>=1:
            dp[i] = max(dp[i], dp[i-1])
        if i>=2:
            dp[i] = max(dp[i], dp[i-2]+arr[i])
    print(dp[-1])

    # max_neg = max(arr)
    # odd_sum = even_sum = 0
    # for i in range(n):
    #     if arr[i]<=0: continue
    #     if i%2:
    #         odd_sum += arr[i]
    #     else:
    #         even_sum += arr[i]
    # print(max(max_neg, odd_sum if odd_sum>0 else -INF, even_sum if even_sum>0 else -INF))

'''
Input:
2
22
-555548351 651494142 -811874594 -656042234 -304130714 -792506758 258253666 610641059 -396748753 122964868 98453969 -376909472 -407159255 995631391 -671355018 833012801 -403932019 8227241 106447332 -882688332 -137524945 -251585166
19
241544047 445524853 264526789 805620292 -867280223 588405847 -389874444 395237189 996661610 863897331 -39551111 -802345706 926471553 111814034 -723611339 187247451 -677523472 -30499890 446727507

Output:
3221971502
3397746997
'''

