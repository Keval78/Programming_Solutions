'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from typing import List
from collections import defaultdict

class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        n = len(nums)
        duplet_sums = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                duplet_sums[(nums[i] + nums[j])%d].append((i, j))

        ans=0 
        for k, num in enumerate(nums):
            for (i, j) in duplet_sums[(-num)%d]:
                if j < k: ans+=1
        
        return ans


