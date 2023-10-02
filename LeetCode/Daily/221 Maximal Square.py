'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from typing import List
import math


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        area = [[0]*m for j in range(n)]
        for i in range(n):
            for j in range(m):
                area[i][j] = int(matrix[i][j])
                if i > 0 and j > 0 and area[i][j] > 0:
                    ms = min(area[i-1][j], area[i-1][j-1], area[i][j-1])
                    area[i][j] = (int(math.sqrt(ms)) + 1)**2

        return max([max(m) for m in area])
