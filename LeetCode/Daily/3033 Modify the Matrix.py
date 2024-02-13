'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])

        col_max = []
        for j in range(m):
            col_max.append(matrix[0][j])
            for i in range(n):
                col_max[-1] = max(col_max[-1], matrix[i][j])
        

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == -1:
                    matrix[i][j] = col_max[j]
        

        return matrix
        