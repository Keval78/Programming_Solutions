'''
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

# https://github.com/Tsuzat/fast-IO-for-python/blob/master/fast_IO/__init__.py

#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase

# region fastio

BUFSIZE: int = 8192

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
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

# from os import path
# from math import log2, floor, ceil, sqrt, pow, gcd
# from random import random, randint, shuffle, choice
# from collections import Counter, defaultdict, deque
# from itertools import permutations, combinations
# from functools import reduce
# from heapq import heapify, heappop, heappush, heapreplace
from bisect import bisect_left, bisect_right, insort


def si(): return input().strip()
def ii(): return int(si())
def mi(ss=" "): return map(int, si().split(ss))
def msi(ss=" "): return map(str, si().split(ss))
def li(ss=" "): return list(mi(ss))


MOD, MOD2, INF = 10 ** 9 + 7, 998244353, float('inf')
MAX = 10**5+1

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.fenwick_tree = [0] * n

    def update(self, k, val):
        while k < self.n:
            self.fenwick_tree[k] += val
            k += (k + 1) & (-(k + 1))

    def pref_sum(self, k):
        s = 0
        while k + 1:
            s += self.fenwick_tree[k]
            k -= (k + 1) & (- (k + 1))
        return s

def solve():
    n = ii()
    arr = []
    for _ in range(n):
        x, y = mi()
        arr.append((x,y))
    
    arr.sort(key=lambda x:x[1])
    # print(arr)
    
    index_map = {}
    for i in range(n):
        index_map[arr[i][1]] = i
    
    arr.sort()
    fenwick = FenwickTree(n)
    
    ans = 0
    for i in range(n):
        ans += i-fenwick.pref_sum(index_map[arr[i][1]])
        fenwick.update(index_map[arr[i][1]], 1)
        # idx = bisect_right(opens, arr[i][1])
        # ans += len(opens)-idx
        # insort(opens, arr[i][1])
    print(ans)

# test = 1
test = ii()
for _ in range(test):
    # print("case", _+1)
    solve()

