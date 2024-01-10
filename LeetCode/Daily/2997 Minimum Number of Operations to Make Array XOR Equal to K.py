'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        
        op = 0
        for i in range(32):
            if (xor%2) != (k%2): op+=1
            xor //= 2 
            k //= 2
        return op