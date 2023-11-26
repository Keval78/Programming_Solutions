'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from typing import List
from collections import defaultdict

class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        MOD = 10**9 + 7
        for i in range(n-1, -1, -1):
            bit = 1 << i
            if a & bit == b & bit:
                a |= bit
                b |= bit
            else:
                if a > b:
                    a, b = b, a
                a |= bit
                b &= ~bit
        
        return (a*b)%MOD


a = 12
b = 5
n = 4
ans = Solution().maximumXorProduct(a, b, n)
print(ans)

a = 6
b = 7
n = 5
ans = Solution().maximumXorProduct(a, b, n)
print(ans)

a = 1
b = 6
n = 3
ans = Solution().maximumXorProduct(a, b, n)
print(ans)

