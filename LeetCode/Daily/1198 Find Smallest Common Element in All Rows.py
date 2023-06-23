"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""
from collections import defaultdict

def main():
    class Solution:
        def smallestCommonElement(self, mat: List[List[int]]) -> int:
            n, m = len(mat), len(mat[0])
            pos = [0]*n
            curr_max, count = 0, 0

            while True:
                for i in range(n):
                    while(pos[i]<m and mat[i][pos[i]]<curr_max):
                        pos[i]+=1
                    if pos[i] >= m: return -1 # return -1 if any position reach to end.
                    if mat[i][pos[i]] != curr_max: 
                        count, curr_max = 1, mat[i][pos[i]]
                    else:
                        count = count+1
                        if count == n: return curr_max

    Solution().smallestCommonElement()


if __name__ == "__main__":
    main()
