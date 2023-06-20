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
    '''
    Proof for the bitwise XOR of two numbers to have Odd Number of set bits only when exactly one of them have odd number of bits?
    I was doing some Algorithms Contest Question ( OffCourse it is not live now), Where I encountered this amazing Pattern that Two Non Negative Numbers 𝐴 and 𝐵
    whose Exclusive XOR represented by 𝐶=𝐴⊕𝐵 is going to have Odd Number of Set bits Only when exactly one of them A or B have odd Number of Set bits for All other cases the C is going to have Even Number of Set Bits..
    You can Take Any example of your wish A=2 and B=9 where A has odd number of set bits and B has even set Bits without even xoring them I can say 𝐴⊕𝐵 is going to have odd number of bits. 
    I am not able to prove it in my head that why is it true? It will appreciated if someone can provide a more concrete proof..
    '''
    for _ in range(ii()):
        n, a = ii(), li()
        def bit_count(x): return bin(x).count("1")
        arr = [bit_count(a[i]) % 2 for i in range(n)]

        ans = 0
        running_sum, odd_pf_cnt, even_pf_cnt = 0, 0, 0

        for num in arr:
            running_sum += num
            if running_sum % 2:
                odd_pf_cnt += 1
                ans += even_pf_cnt + 1
            else:
                even_pf_cnt += 1
                ans += odd_pf_cnt
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
def input(): return sys.stdin.readline().rstrip("\r\n")


# endregion

if __name__ == "__main__":
    # read()
    main()


# * PROBLEM DESCERIPTION
# link :- https://www.hackerearth.com/challenges/competitive/june-circuits-23/algorithm/count-subarrays-3-ba2ff701/
# Test Input
'''
1
3
1 2 4
'''
