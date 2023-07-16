'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from __future__ import division, print_function
from cmath import inf

import os
import sys
from io import BytesIO, IOBase
from collections import defaultdict, Counter
from os import path
from math import log2, floor, ceil, sqrt, pow, gcd
# from random import random, randint, shuffle, choice
from collections import Counter, defaultdict, deque
# from itertools import permutations, combinations
# from functools import reduce
# from heapq import heapify, heappop, heappush, heapreplace
# from bisect import bisect_left, bisect_right


def ii(): return int(input())
def si(): return input()
def mi(ss=" "): return map(int, input().strip().split(ss))
def msi(ss=" "): return map(str, input().strip().split(ss))
def li(ss=" "): return list(mi(ss))


def read():
    sys.stdin = open('./input.txt', 'r')
    sys.stdout = open('./output.txt', 'w')


MOD, MOD2, INF = 10 ** 9 + 7, 998244353, float('inf')

# BRUTE FORCE....

# text = iter('''3
# 4 4
# -2 -5 -3 4
# 5 14
# -5 2 -4 3 -3
# 6 14
# -3 -5 1 1 -7 2'''.split("\n"))

# def si(): return next(text).strip()
# def ii(): return int(si())
# def mi(ss=" "): return map(int, si().split(ss))
# def msi(ss=" "): return map(str, si().split(ss))
# def li(ss=" "): return list(mi(ss))


# def solve(curr_sum, curr_op, visited):
#     # print(curr_sum, curr_op, visited)
#     global n, k, arr, min_op
#     if curr_sum >= k:
#         min_op = min(min_op, curr_op)
#         return

#     for i in range(n-1):
#         if arr[i] not in visited and arr[i+1] not in visited:
#             solve(curr_sum - 2*(arr[i]+arr[i+1]), curr_op+1, visited + [arr[i],arr[i+1]])


# for _ in range(ii()):
#     n, k = mi()
#     arr = li()
#     # print(n, k)
#     # print(arr)
#     min_op = float('inf')
#     solve(sum(arr), 0, [])
#     if min_op > n: min_op = -1
#     print(min_op)


def main():
    for _ in range(ii()):
        n, x = mi()
        arr = li()
        # print(n, x)
        # print(arr, [x^i for i in arr])

        dp = [[0 for i in range(n)] for j in range(2)]
        for j in range(1, n):
            for i in range(2):
                curr = arr[j] ^ x if i != 0 else arr[j]
                # print(dp[0][j-1] + abs(curr-arr[j-1]), dp[1][j-1] + abs(curr-(arr[j-1]^x)))
                dp[i][j] = max(dp[0][j-1] + abs(curr-arr[j-1]),
                               dp[1][j-1] + abs(curr-(arr[j-1] ^ x)))
        print(max(dp[0][n-1], dp[1][n-1]))


# region fastio
# template taken from https://github.com/cheran-senthil/PyRival/blob/master/templates/template.py
BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


def print(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop("end", "\n"))
    if kwargs.pop("flush", False):
        file.flush()


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
def input(): return sys.stdin.readline().rstrip("\r\n")


# endregion

if __name__ == "__main__":
    # read()
    main()


# * PROBLEM DESCERIPTION
# link :- https://www.hackerearth.com/challenges/competitive/july-circuits-23/algorithm/xor-or-not-f0540578/
# Test Input
