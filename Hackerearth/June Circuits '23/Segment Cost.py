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


def ii(): return int(input())
def si(): return input()
def mi(ss=" "): return map(int, input().strip().split(ss))
def msi(ss=" "): return map(str, input().strip().split(ss))
def li(ss=" "): return list(mi(ss))


def read():
    sys.stdin = open('./input.txt', 'r')
    sys.stdout = open('./output.txt', 'w')


def main():
    n = ii()
    arr = li()
    x, y = mi()

    prefix_sum = [i for i in range(n+1)]
    prefix_xor = [i for i in range(n+1)]

    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + arr[i]
        prefix_xor[i+1] = prefix_xor[i] ^ arr[i]

    print(prefix_sum)
    print(prefix_xor)
    print([0]+arr)
    print([i for i in range(n+1)])
    # for i in range(x, y+1):
    #     val = (prefix_sum[i]-prefix_sum[x-1]) - (prefix_xor[i]^prefix_xor[x-1])
    #     print(prefix_sum[i]-prefix_sum[x-1], prefix_xor[i]^prefix_xor[x-1])
    #     print("s", val)

    ans = (prefix_sum[y]-prefix_sum[x-1]) - (prefix_xor[y] ^ prefix_xor[x-1])


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
# link :- https://www.hackerearth.com/challenges/competitive/june-circuits-23/algorithm/segment-cost-af31ef0c/
# Test Input
'''
2
5 10
1 2
'''
