'''
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

# from collections import Counter, defaultdict

# import maths functions & constants
# from math import gcd
# from cmath import inf

# import functools.
# from functools import reduce

# import Generic Type
from typing import List


def ii(): return int(input())
def si(): return input()
def mi(ss=" "): return map(int, input().strip().split(ss))
def msi(ss=" "): return map(str, input().strip().split(ss))
def li(ss=" "): return list(mi(ss))


def main():
    class Solution:
        def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
            ranges = []

            for idx, num in enumerate(nums):
                sub_range_lower = lower
                sub_range_upper = num

                if sub_range_lower != sub_range_upper:
                    if sub_range_lower == sub_range_upper-1:
                        ranges.append(str(sub_range_lower))
                    else:
                        ranges.append(
                            f"{sub_range_lower}->{sub_range_upper-1}")
                lower = sub_range_upper + 1

            if lower <= upper:
                if lower == upper:
                    ranges.append(str(lower))
                else:
                    ranges.append(str(lower)+"->"+str(upper))
            return ranges

    Solution().findMissingRanges(
        nums=[0, 1, 3, 50, 75], lower=0, upper=99)


if __name__ == "__main__":
    main()
