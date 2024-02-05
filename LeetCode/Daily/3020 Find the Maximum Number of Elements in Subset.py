'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List
from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        MAX = 10**9+7
        cntr = Counter(nums)
        ans = cntr.get(1, 0)
        for num in cntr:
            val, l = num, 0
            # print(val, l)
            while val != 1 and val in cntr:
                l += min(cntr[val], 2)
                if cntr[val] == 1: break
                val *= val
            # print(val, l)
            ans = max(ans, l)
        return ans if ans%2 else ans-1


nums = [5,4,1,2,2]
ans = Solution().maximumLength(nums)
print(ans)

nums = [1,3,2,4]
ans = Solution().maximumLength(nums)
print(ans)

nums = [1,1]
ans = Solution().maximumLength(nums)
print(ans)

nums = [14,14,196,196,38416,38416]
ans = Solution().maximumLength(nums)
print(ans)

nums = [1,1,1,1,1,1,1,1,1,1,2,4,8,16,32,64,128,256,512,1024]
ans = Solution().maximumLength(nums)
print(ans)
