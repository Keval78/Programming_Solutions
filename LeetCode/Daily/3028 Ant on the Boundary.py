'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List
class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        n = len(nums)
        cnt, pos = 0, n

        for num in nums:
            pos += num
            if pos == n:
                cnt += 1

        return cnt
        