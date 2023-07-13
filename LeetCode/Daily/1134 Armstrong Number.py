'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
import re
class Solution:
    def isArmstrong(self, n: int) -> bool:
        total, k = n, 0
        while n:
            k+=1
            n //= 10
        n = total
        while n:
            total -= (n%10)**k
            n //= 10
        return total == 0
