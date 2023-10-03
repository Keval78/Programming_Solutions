'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

import math
from typing import List
# from collections import defaultdict

# sys.setrecursionlimit(10 ** 5)
MOD, MOD2, INF = 10 ** 9 + 7, 998244353, float('inf')
MAX = 10**5+1


class SparseTable:
    def __init__(self):
        self.sp_table = []
        self.K = 0
        self.LIMIT = 10**9
        self.bin_log = [0 for i in range(MAX)]

    def build(self, arr, n):
        self.K = int(math.log2(n) + 1)
        # print(self.K)
        self.bin_log[1] = 0
        for i in range(2, n+1):
            self.bin_log[i] = self.bin_log[i//2]+1
        self.sp_table = [[0 for _ in range(n)] for _ in range(self.K)]

        for i in range(n):
            self.sp_table[0][i] = arr[i]

        for i in range(1, self.K):
            for j in range(n - (1 << i) + 1):
                self.sp_table[i][j] = max(
                    self.sp_table[i-1][j],
                    self.sp_table[i-1][j + (1 << (i-1))],
                )

        # for i in self.sp_table:
        #     print(i)

    def getmax(self, L, R):
        length = R-L+1
        k = self.bin_log[length]
        # print(k, L, R-(1<<k)+1)#, self.sp_table[k][L], self.sp_table[k][R-(1<<k)+1])
        # print(max(self.sp_table[k][L], self.sp_table[k][R-(1 << k)+1]))
        return max(self.sp_table[k][L], self.sp_table[k][R-(1 << k)+1])


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        s = SparseTable()
        s.build(nums, n)

        ans = 0
        for j in range(1, n-1):
            i_max = s.getmax(0, j-1)
            k_max = s.getmax(j+1, n-1)

            ans = max(ans, (i_max - nums[j]) * k_max)

        return ans
