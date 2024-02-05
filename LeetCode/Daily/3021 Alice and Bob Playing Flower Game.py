'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List
from collections import Counter

class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        cntr = Counter()
        ans = 0
        
        # Odd - Even pair
        ans += ((n+1)//2) * (m//2)
        
        # Even - Odd pair
        ans += (n//2) * ((m+1)//2)
        
        return ans


n = 3
m = 2
ans = Solution().flowerGame(n, m)
print(ans)

n = 1
m = 1
ans = Solution().flowerGame(n, m)
print(ans)
