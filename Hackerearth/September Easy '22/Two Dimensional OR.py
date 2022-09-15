from __future__ import division, print_function
from cmath import inf
from curses.ascii import isdigit

import os,sys
from re import L
from io import BytesIO, IOBase
from collections import defaultdict
import collections
# import numpy as np



def ii():  return int(input())
def si():  return input()
def mi(ss=" "):  return map(int,input().strip().split(ss))
def msi(ss=" "): return map(str,input().strip().split(ss))
def li(ss=" "):  return list(mi(ss))



def read():
    sys.stdin  = open('./input.txt', 'r')
    sys.stdout = open('./output.txt', 'w')

def main():
    n, m = mi()
    arr = [li() for j in range(n)]
    
    bit_range = 30
    
    # pref = np.zeros((bit_range, n, m), dtype=np.uint32)
    pref = [[[0 for i in range(m)] for j in range(n)] for k in range(bit_range)]
    
    for bit in range(bit_range):
        for i in range(n):
            for j in range(m):
                if arr[i][j] & (1<<bit):
                    pref[bit][i][j] += 1
    
    for bit in range(bit_range):
        for i in range(1,n):
            pref[bit][i][0] += pref[bit][i-1][0]
        for j in range(1,m):
            pref[bit][0][j] += pref[bit][0][j-1]
        for i in range(1,n):
            for j in range(1,m):
                pref[bit][i][j] += pref[bit][i-1][j] + pref[bit][i][j-1] - pref[bit][i-1][j-1]
                    
    # print(pref)
    
    for q in range(ii()):
        x1, y1, x2, y2 = mi()
        
        ans = 0
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        for bit in range(bit_range):
            bits = pref[bit][x2][y2]
            if x1-1 > 0:
                bits -= pref[bit][x1-1][y1]
            if y1-1 > 0:
                bits -= pref[bit][x1][y1-1]
            if (x1-1) > 0 and (y1-1) > 0:
                bits += pref[bit][x1-1][y1-1]
            if bits > 0:
                ans |= (1<<bit)
        
        print(ans)
    return























    


















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
input = lambda: sys.stdin.readline().rstrip("\r\n")


# endregion

if __name__ == "__main__":
    read()
    main()




# * PROBLEM DESCERIPTION
# link :- https://www.hackerearth.com/challenges/competitive/september-easy-22/algorithm/two-dimensional-or-daa0a7aa/
# Test Input
'''
3 3
1 2 3
4 5 6
7 8 9
2
1 1 3 3
1 2 1 3
'''
