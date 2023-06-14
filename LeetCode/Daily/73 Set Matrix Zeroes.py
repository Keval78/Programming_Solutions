'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

def main():
    class Solution:
        def setZeroes(self, matrix: List[List[int]]) -> None:
            """
            Do not return anything, modify matrix in-place instead.
            """
            first_row_ele, first_col_ele = False, False
            
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if matrix[i][j] == 0:
                        matrix[0][j] = 0
                        matrix[i][0] = 0
                        if i==0: first_row_ele = True
                        if j==0: first_col_ele = True
            for i in range(1, len(matrix)):
                if matrix[i][0] == 0:
                    for j in range(len(matrix[i])):
                        matrix[i][j] = 0
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0:
                    for i in range(len(matrix)):
                        matrix[i][j] = 0
            if first_col_ele:
                for i in range(len(matrix)):
                    matrix[i][0] = 0
            if first_row_ele:
                for j in range(len(matrix[0])):
                    matrix[0][j] = 0
            
            return matrix
    Solution().setZeroes()


if __name__ == "__main__":
    main()



