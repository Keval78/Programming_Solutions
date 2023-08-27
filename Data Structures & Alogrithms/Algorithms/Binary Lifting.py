"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

# Binary Lifting
import math
from typing import List

MOD, MOD2, INF = 10 ** 9 + 7, 998244353, float('inf')
MAX = 10**5+1


class BinaryLifting:
    """
    Table for Binary Lifting
    """

    def __init__(self, parents: List[int]):
        n = len(parents)
        k = n.bit_length() + 1

        bl_table = [[-1 for _ in range(n)] for _ in range(k)]

        for i in range(n):
            bl_table[0][i] = parents[i]

        for i in range(1, k):
            for j in range(n):
                if bl_table[i-1][j] == -1:
                    bl_table[i][j] = -1
                else:
                    bl_table[i][j] = bl_table[i-1][bl_table[i-1][j]]

        self.bl_table = bl_table

    def getkthancestor(self, node, k):
        # walk on binary of k.
        # self.blTable
        j = 1
        while k > 0:
            if k & 1:
                node = self.bl_table[j][node]
            j = j << 1
            k = k >> 1
            if node == -1:
                return node
        return node
