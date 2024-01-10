'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        lsp = l = 0
        i, n = 0, len(nums)
        while i < n: 
            start = i
            while i<n and (start==i or nums[i] == nums[i-1]+1): i+=1
            
            if l < i-start:
                l = i-start
                lsp = sum(nums[start: i])
            break
        
        # print(lsp)
        num = lsp
        while True:
            if num not in nums: return num
            num+=1
        
        