'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n = len(mountain)
        indices = []
        for i in range(1, n-1):
            if mountain[i-1] < mountain[i] < mountain[i+1]:
                indices.append(i)
        
        return indices
        



mountain = [2,4,4]
ans = Solution().findPeaks(mountain)
print(ans)


mountain = [1,4,3,8,5]
ans = Solution().findPeaks(mountain)
print(ans)


