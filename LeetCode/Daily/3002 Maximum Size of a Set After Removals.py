'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        s1, s2 = set(nums1),set(nums2)

        if len(s1) <= n//2 and len(s2) <= n//2:
            return len(s1|s2)
        else:
            if len(s1) <= n//2:
                uniq = set()
                for ele in s2:
                    if ele not in s1:
                        uniq.add(ele)
                        if len(uniq) == n//2: break

                uniq.update(s1)
                return len(uniq)
            
            elif len(s2) <= n//2:
                uniq = set()
                for ele in s1:
                    if ele not in s2:
                        uniq.add(ele)
                        if len(uniq) == n//2: break

                uniq.update(s2)
                return len(uniq)
            
            else:
                uniq = set()
                for ele in s1:
                    if ele not in uniq:
                        uniq.add(ele)
                        if len(uniq) == n//2: break
                
                print(uniq)
                for ele in s2:
                    if ele not in uniq:
                        uniq.add(ele)
                        if len(uniq) == n: break
                
                print(uniq)
                
                return len(uniq)


nums1 = [3, 4]
nums2 = [8, 9]
ans = Solution().maximumSetSize(nums1, nums2)
print(ans)

nums1 = [7,1,5,4,2,5,7,2,10,9]
nums2 = [8,2,4,1,4,5,9,9,6,6]
ans = Solution().maximumSetSize(nums1, nums2)
print(ans)