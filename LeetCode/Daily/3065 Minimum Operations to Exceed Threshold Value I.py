'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum([1 for i in nums if i<k])
        