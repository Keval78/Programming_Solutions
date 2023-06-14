'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from collections import Counter

def main():
    class Solution:
        def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
            i, j = 0, 0
            rows, cols = [0, len(matrix)], [0, len(matrix[0])]
            spiral = []

            
            while rows[0]<rows[1] and cols[0]<cols[1]:
                for j in range(cols[0], cols[1]):
                    spiral.append(matrix[i][j])
                rows[0]+=1
                #print(spiral, rows, cols)
                if rows[0]>=rows[1] or cols[0]>=cols[1]: break
                
                for i in range(rows[0], rows[1]):
                    spiral.append(matrix[i][j])
                cols[1]-=1
                #print(spiral, rows, cols)
                if rows[0]>=rows[1] or cols[0]>=cols[1]: break

                for j in range(cols[1]-1, cols[0]-1, -1):
                    spiral.append(matrix[i][j])
                rows[1]-=1
                #print(spiral, rows, cols)
                if rows[0]>=rows[1] or cols[0]>=cols[1]: break
                
                for i in range(rows[1]-1, rows[0]-1, -1):
                    spiral.append(matrix[i][j])
                cols[0]+=1
                #print(spiral, rows, cols)
            return spiral
    Solution().spiralOrder()


if __name__ == "__main__":
    main()



