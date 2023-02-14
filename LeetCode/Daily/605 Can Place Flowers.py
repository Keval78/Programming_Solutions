'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

#import collections
from collections import Counter, defaultdict

# import maths functions & constants
from math import gcd
from cmath import inf

# import functools.
from functools import reduce

# import Generic Type
from typing import Generic, TypeVar


def ii():  return int(input())
def si():  return input()
def mi(ss=" "):  return map(int,input().strip().split(ss))
def msi(ss=" "): return map(str,input().strip().split(ss))
def li(ss=" "):  return list(mi(ss))


def main():
    class Solution:
        def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
            n_plants, lazycount = 0, 0
            flowerbed = [0]+flowerbed+[0]
            for i in range(len(flowerbed)):
                if flowerbed[i] == 1: n_plants, lazycount = n_plants + max(0,((lazycount-1)//2)), 0
                else: lazycount += 1
            n_plants, lazycount = n_plants + max(0,((lazycount-1)//2)), 0
            return n_plants >= n

            '''
            count = 0
            for i in range(len(flowerbed)):
                # Check if the current plot is empty.
                if flowerbed[i] == 0:
                    # Check if the left and right plots are empty.
                    empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                    empty_right_lot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                    
                    # If both plots are empty, we can plant a flower here.
                    if empty_left_plot and empty_right_lot:
                        flowerbed[i] = 1
                        count += 1
                        if count >= n:
                            return True
            return count >= n
            '''
    
    Solution().canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1)


if __name__ == "__main__":
    main()
