from __future__ import division, print_function
from cmath import inf

import os,sys
from io import BytesIO, IOBase

def ii():  return int(input())
def si():  return input()
def mi(ss=" "):  return map(int,input().strip().split(ss))
def msi(ss=" "): return map(str,input().strip().split(ss))
def li(ss=" "):  return list(mi(ss))



def read():
    sys.stdin  = open('./input.txt', 'r')
    sys.stdout = open('./output.txt', 'w')


def main():
    matchsticks = [14,10,10,10,10,10,10,10,10,10,10,10,8,9,19]
    if not matchsticks:
        return False
    sides = [0,0,0,0]
    n = len(matchsticks)    
    total = sum(matchsticks)
    if(total % 4):
        return False    
    target = total // 4
    
    matchsticks.sort(reverse=True)
       
    def backtrack(i):
        if i==n:
            return True
        for j in range(4):
            if(sides[j] + matchsticks[i] <= target):    
                sides[j] += matchsticks[i]
                if(backtrack(i + 1)):
                    return True
                sides[j] -= matchsticks[i]
        return False
    return backtrack(0)
    '''
    def makesquare(self, nums):
        nums = matchsticks
        if not nums:
            return False

        L = len(nums)
        perimeter = sum(nums)
        possible_side =  perimeter // 4
        if possible_side * 4 != perimeter:
            return False

        nums.sort(reverse=True)
        sums = [0 for _ in range(4)]

        def dfs(index):
            if index == L:
                return sums[0] == sums[1] == sums[2] == possible_side
            for i in range(4):
                if sums[i] + nums[index] <= possible_side:
                    sums[i] += nums[index]
                    if dfs(index + 1):
                        return True
                    sums[i] -= nums[index]
            return False        
        return dfs(0)
    '''
    
        
        
            
        
        

        
        
            























    


















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
# link :- https://leetcode.com/problems/matchsticks-to-square/
# Test Input
'''
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
'''
