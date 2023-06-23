"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

def main():
    class Solution:
        def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
            m, n, p = len(mat1), len(mat2), len(mat2[0])
            mat = [[0 for j in range(p)] for i in range(m)]
            for i in range(m):
                for j in range(n):
                    for k in range(p):
                        mat[i][k] += mat1[i][j]*mat2[j][k]
            return mat


    Solution().multiply()


if __name__ == "__main__":
    main()
