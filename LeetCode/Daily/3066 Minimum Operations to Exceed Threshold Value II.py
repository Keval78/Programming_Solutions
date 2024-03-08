'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List
from heapq import heapify, heappop, heappush

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        
        op = 0
        while len(nums) > 1:
            x, y = heappop(nums), heappop(nums)
            if x >= k: break
            
            heappush(nums, 2*x+y)
            op += 1
        return op
                
            
        
            
        