#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  TEMP.py
#
#################### I/O SECTION ####################
import threading
import time
start = time.time()
import sys
fastio = sys.stdin.readline


def inp():
    return(int(fastio()))
def inlt():
    return(list(map(int,fastio().split())))
def insr():
    s = fastio()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,fastio().split()))

#################### CODE SECTION ####################

def adder():
    print(sum(invr()))

def subber():
    import math
    print(math.prod(invr()))


for _ in range(int(inp())):

    t1 = threading.Thread(target=adder, args=())
    t2 = threading.Thread(target=subber, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()


#################### EXECUTION ####################

def main(args):
    return 0

print (time.time()- start)

if __name__ == '__main__':
    sys.exit(main(sys.argv))