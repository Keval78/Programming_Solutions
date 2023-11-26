'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from typing import List
from collections import defaultdict

class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        zero_cnt = s.count('0')
        
        moves = 0
        for i in range(n):
            if s[i] == "1":
                moves += zero_cnt
            else:
                zero_cnt -= 1
        
        return moves


s = "101"
ans = Solution().minimumSteps(s)
print(ans)

s = "100"
ans = Solution().minimumSteps(s)
print(ans)

s = "0111"
ans = Solution().minimumSteps(s)
print(ans)

