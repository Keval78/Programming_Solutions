'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List
from collections import defaultdict, Counter

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        cntr = defaultdict(int)
        for num in arr1:
            snum = str(num)
            for i in range(len(snum)):
                cntr[int(snum[:i+1])] = 1
        
        ans = 0
        for num in arr2:
            snum = str(num)
            for i in range(len(snum)):
                if cntr[int(snum[:i+1])] > 0:
                    ans = max(ans, i+1)

        return ans


        

arr1 = [1,10,100]
arr2 = [1000]
ans = Solution().longestCommonPrefix(arr1, arr2)
print(ans)

arr1 = [1,2,3]
arr2 = [4,4,4]
ans = Solution().longestCommonPrefix(arr1, arr2)
print(ans)
