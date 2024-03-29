# CourseCode : AISC_1000
# FirstName  : Keval
# LastName   : Padsala
# Student#   : 500199506
# Assignmwnt : Case Study 01 S21

from __future__ import division, print_function

import os,sys
from io import BytesIO, IOBase

if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip

def validate_input(num_grade):
    if num_grade.isnumeric():
        if int(num_grade) <= 100 and int(num_grade) >= 0:
            return True
        else:
            print(num_grade,"Input must be between 0 and 100")
            return False
    else:
        print(num_grade,"Input is not Numeric. Please Enter Valid input")
        return False

    # Testing
    # print("")

def grade_system(num_grade):
    # print(num_grade)
    if num_grade < 60:
        return "F"
    elif num_grade < 67:
        return "D"
    elif num_grade < 80:
        return "C"
    elif num_grade < 88:
        return "B"
    else:
        return "A"
    
# def si():  return input()

def main():

    print("Letter Grade Converter")
    # print("Enter numerial grade:")

    checker = True
    while checker:
        print("Enter numerial grade:", end=" ")
        num_grade = si()
        print(num_grade)
        if validate_input(num_grade): # return True or False
            print(grade_system(int(num_grade))) # Grade_

        print("Continue?", end=" ")
        con = si()
        print(con)
        if(con == "Y" or con == "y"):
            continue
        else:
            print("Bye!")
            break
        
        
        
    















###### region fastio ######
###### template taken from https://github.com/cheran-senthil/PyRival/blob/master/templates/template.py ######
###### Author : Keval_78
###### Date   : 7th OCT 2021

def ii():  return int(input())
def si():  return input()
def mi(ss=" "):  return map(int,input().strip().split(ss))
def msi(ss=" "): return map(str,input().strip().split(ss))
def li(ss=" "):  return list(mi(ss))

def dmain():
    sys.setrecursionlimit(1000000)
    threading.stack_size(1024000)
    thread = threading.Thread(target=main)
    thread.start()

#from collections import deque, Counter, OrderedDict,defaultdict
#from heapq import nsmallest, nlargest, heapify,heappop ,heappush, heapreplace
#from math import log,sqrt,factorial,cos,tan,sin,radians
#from bisect import bisect,bisect_left,bisect_right,insort,insort_left,insort_right
#from decimal import *
#import threading
#from itertools import permutations
#Copy 2D list  m = [x[:] for x in mark] .. Avoid Using Deepcopy


def read():
    sys.stdin  = open('../input.txt', 'r')  
    sys.stdout = open('../output.txt', 'w') 


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


if sys.version_info[0] < 3:
    sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
else:
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

input = lambda: sys.stdin.readline().rstrip("\r\n")

###### endregion ######



if __name__ == "__main__":
    read()
    main()
    #dmain()
