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


# sys.setrecursionlimit(10 ** 5)
MOD, MOD2, INF = 10 ** 9 + 7, 998244353, float('inf')
MAX = 10**5+1

import math

for _ in range(ii()):
    n = ii()
    arr = li()

    results = {}
    divisors, nextDivisors = {}, {}
    for i in range(n):
        nextDivisors.clear()
        for p, count in divisors.items():
            next_lcm = (p*arr[i])//math.gcd(p, arr[i])
            if next_lcm > MOD: continue
            nextDivisors[next_lcm] = nextDivisors.get(next_lcm, 0) + count
        nextDivisors[arr[i]] = nextDivisors.get(arr[i], 0) + 1

        divisors, nextDivisors = nextDivisors, divisors
        for p, count in divisors.items():
            results[p] = results.get(p, 0) + count

    ans = 0
    x, y = mi()
    for p, count in results.items():
        if x <= p <= y:
            ans += count
    print(ans)


# class SparseTable:
#     def __init__(self):
#         self.spTable = []
#         self.K = 0
#         self.LIMIT = 10**9

#     def init(self, a, n):
#         self.K = int(math.log2(n) + 2)
#         self.spTable = [[1 for _ in range(n)] for _ in range(self.K + 1)]

#         for i in range(n):
#             self.spTable[0][i] = a[i]

#         for i in range(1, self.K + 1):
#             for j in range(n - (1 << i) + 1):
#                 if self.spTable[i - 1][j] == -1:
#                     self.spTable[i][j] = -1
#                 elif self.spTable[i - 1][j + (1 << (i - 1))] == -1:
#                     self.spTable[i][j] = -1
#                 else:
#                     self.spTable[i][j] = (self.spTable[i - 1][j] * self.spTable[i - 1][j + (1 << (i - 1))]) // math.gcd(self.spTable[i - 1][j], self.spTable[i - 1][j + (1 << (i - 1))])

#                 if self.spTable[i][j] > self.LIMIT:
#                     self.spTable[i][j] = -1

#     def getLCM(self, L, R):
#         i = int(math.log2(R - L + 1))
#         if self.spTable[i][L] == -1: return -1
#         if self.spTable[i][R - (1 << i) + 1] == -1: return -1

#         return (self.spTable[i][L] * self.spTable[i][R - (1 << i) + 1] // math.gcd(self.spTable[i][L], self.spTable[i][R - (1 << i) + 1]))


# def main():
#     obj = SparseTable()
#     for _ in range(ii()):
#         N = ii()
#         A = li()
#         X, Y = mi()
#         obj.init(A, N)

#         ans = 0
#         for i in range(N):
#             j, k = i + 1, i - 1
#             low, high = i, N - 1
#             while low <= high:
#                 mid = (low + high) // 2
#                 if obj.getLCM(i, mid) >= X or obj.getLCM(i, mid) < 0:
#                     j = mid
#                     high = mid - 1
#                 else:
#                     j = mid + 1
#                     low = mid + 1

#             low, high = i, N - 1
#             while low <= high:
#                 mid = (low + high) // 2
#                 if obj.getLCM(i, mid) > Y or obj.getLCM(i, mid) < 0:
#                     high = mid - 1
#                 else:
#                     k = mid
#                     low = mid + 1
#             ans += max(k - j + 1, 0)
#         print(ans)

# if __name__ == "__main__":
#     main()
