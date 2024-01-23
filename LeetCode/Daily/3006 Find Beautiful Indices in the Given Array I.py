'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List
from bisect import bisect_left, bisect

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n = len(s)
        a_indices = []
        b_indices = []

        for i in range(n):
            if s[i:i+len(a)] == a:
                a_indices.append(i)
            if s[i:i+len(b)] == b:
                b_indices.append(i)

        indices = []
        for ind in a_indices:
            left = bisect_left(b_indices, ind-k)
            right = bisect(b_indices, ind+k)

            if right-left > 0:
                indices.append(ind)
        
        return indices
        

            
        
        

s = "isawsquirrelnearmysquirrelhouseohmy"
a = "my"
b = "squirrel"
k = 15
ans = Solution().beautifulIndices(s, a, b, k)
print(ans)

s = "abcd"
a = "a"
b = "a"
k = 4
ans = Solution().beautifulIndices(s, a, b, k)
print(ans)
