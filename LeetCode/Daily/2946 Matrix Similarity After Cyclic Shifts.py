'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n , m= len(mat), len(mat[0])
        k = k%m
        for i in range(0, n, 2):
            if mat[i] != mat[i][k:] + mat[i][:k]:
                return False
        
        for i in range(1, n, 2):
            if mat[i] != mat[i][m-k:] + mat[i][:m-k]:
                return False
        return True


mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]]
k = 2
ans = Solution().areSimilar(mat, k)
print(ans)


mat = [[2,2],[2,2]]
k = 3
ans = Solution().areSimilar(mat, k)
print(ans)

mat = [[1,2]]
k = 1
ans = Solution().areSimilar(mat, k)
print(ans)

mat = [[2,4],[9,8]]
k = 9
ans = Solution().areSimilar(mat, k)
print(ans)

