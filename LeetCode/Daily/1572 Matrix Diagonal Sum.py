'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from collections import Counter

def main():
    class Solution:
        def diagonalSum(self, mat: List[List[int]]) -> int:
            diag_sum = 0
            for i in range(len(mat)):
                diag_sum += mat[i][i]
                diag_sum += mat[-i-1][i]
            return diag_sum if len(mat)%2==0 else diag_sum-mat[len(mat)//2][len(mat)//2]

    Solution().diagonalSum()


if __name__ == "__main__":
    main()
