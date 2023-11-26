'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from typing import List
from collections import defaultdict

class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        eqlen = 0
        for i in range(min(len(s1), len(s2), len(s3))):
            if s1[i] == s2[i] == s3[i]:
                eqlen+=1
            else:
                break

        delchar = len(s1) - eqlen + len(s2) - eqlen + len(s3) - eqlen
        return delchar if eqlen > 0 else -1
        


s1 = "dac"
s2 = "bac"
s3 = "cac"
ans = Solution().findMinimumOperations(s1, s2, s3)
print(ans)

s1 = "abc"
s2 = "abb"
s3 = "ab"
ans = Solution().findMinimumOperations(s1, s2, s3)
print(ans)


s1 = "a"
s2 = "a"
s3 = "a"
ans = Solution().findMinimumOperations(s1, s2, s3)
print(ans)
