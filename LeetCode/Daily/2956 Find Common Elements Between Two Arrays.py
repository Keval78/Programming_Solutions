'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans = [0, 0]
        flag1, flag2 = [False]*101, [False]*101
        
        for num in nums1:
            flag1[num] = True
        
        for num in nums2:
            flag2[num] = True
        
        for num in nums1:
            if flag2[num]: ans[0] += 1
        
        for num in nums2:
            if flag1[num]: ans[1] += 1
        
        return ans


nums1 = [4,3,2,3,1]
nums2 = [2,2,5,2,3,6]
ans = Solution().findIntersectionValues(nums1, nums2)
print(ans)

nums1 = [3,4,2,3]
nums2 = [1,5]
ans = Solution().findIntersectionValues(nums1, nums2)
print(ans)

