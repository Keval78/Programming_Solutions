'''
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List


class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        res = []
        stbg = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        # DP with Memoization
        # def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        #     # DP with Memoization.
        #     def digitdp(idx: int, tight1: int, tight2: int, num1: str, num2: str):
        #         print(idx, tight1, tight2, num1, num2)
        #         if idx == len(num2):
        #             return 1

        #         if memo[idx][tight1][tight2] != -1:
        #             return memo[idx][tight1][tight2]

        #         lo = ord(num1[idx]) - ord('0') if tight1 else 0
        #         hi = ord(num2[idx]) - ord('0') if tight2 else 9
        #         # print(lo, hi)
        #         res = 0
        #         for i in range(lo, hi+1):
        #             res += digitdp(idx+1, tight1 & (i == lo),
        #                            tight2 & (i == hi), num1, num2)

        #         memo[idx][tight1][tight2] = res
        #         return res

        #     num1 = '0'*(len(num2) - len(num1)) + num1

        #     memo = [[[[-1]*(max_sum+1) for i in range(2)]
        #              for j in range(2)] for k in range(23)]
        #     ans1 = digitdp(0, 1, 1, num1, num2)

        #     return ans
