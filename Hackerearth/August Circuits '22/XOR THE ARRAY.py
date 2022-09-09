from __future__ import division, print_function
from cmath import inf

import os,sys
from io import BytesIO, IOBase
from collections import defaultdict
import collections



def ii():  return int(input())
def si():  return input()
def mi(ss=" "):  return map(int,input().strip().split(ss))
def msi(ss=" "): return map(str,input().strip().split(ss))
def li(ss=" "):  return list(mi(ss))



def read():
    sys.stdin  = open('./input.txt', 'r')
    sys.stdout = open('./output.txt', 'w')

def main():
    N = ii()
    arr = li()
    
    if sum(arr) == 0:
        print("0")
    xor = arr[0]
    for i in range(1,N):
        xor ^= arr[i]
    if xor == 0:
        print("1")
    else:
        print("2")
        
        
        
        
        
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
# link :- https://www.hackerearth.com/challenges/competitive/august-circuits-22/algorithm/xor-the-array-77ec971c/
# Test Input
'''
2
3
1 2 3
10
1 1 1 2 2 2 3 3 3 3
'''
