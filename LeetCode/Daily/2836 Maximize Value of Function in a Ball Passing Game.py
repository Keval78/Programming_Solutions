"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

from typing import List


class TreeAncestor:
    def __init__(self, n, parent, k):
        n = len(parent)
        k = k.bit_length() + 1

        # Store [parent, cost] in Binary Lifting
        bl_table = [[[-1, 0] for _ in range(n)] for _ in range(k)]

        for i in range(n):
            bl_table[0][i] = [parent[i], i + parent[i]]

        for i in range(1, k):
            for j in range(n):
                p, c = bl_table[i-1][j]
                pp, pc = bl_table[i-1][p]
                bl_table[i][j] = [pp, pc + c - p]

        self.bl_table = bl_table

    def getKthAncestor(self, node: int, k: int) -> int:
        # walk on binary of k.
        j = 0
        cost = 0
        while k > 0:
            # print(k, j, k&1, self.bl_table[j][node])
            if k & 1:
                node, c = self.bl_table[j][node]
                cost += c - node
            j += 1
            k = k >> 1

        return cost + node


class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        obj = TreeAncestor(len(receiver), receiver, k)
        ans = -1
        for i in range(len(receiver)):
            ans = max(ans, obj.getKthAncestor(i, k))

        return ans
