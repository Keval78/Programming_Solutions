'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        arr = [0]*(n-1)
        for i in range(n-1):
            if nums[i] < nums[i+1]:
                arr[i] = 1
            elif nums[i] > nums[i+1]:
                arr[i] = -1
        
        # print(arr, pattern)
        
        def compute_temporary_array(pattern):
            lps = [0] * len(pattern)
            index, i = 0, 1
            while i < len(pattern):
                if pattern[i] == pattern[index]:
                    lps[i] = index + 1
                    index += 1
                    i += 1
                else:
                    if index != 0: index = lps[index - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        def kmp(text, pattern):
            lps = compute_temporary_array(pattern)
            i, j = 0, 0
            indices = []
            while i < len(text) and j < len(pattern):
                if text[i] == pattern[j]:
                    i, j = i+1, j+1
                else:
                    if j != 0: j = lps[j - 1]
                    else: i += 1
                if j == len(pattern):
                    indices.append(i - len(pattern))
                    j = lps[j - 1]
            return indices
        # print(kmp(arr, pattern))

        return len(kmp(arr, pattern))



nums = [1,2,3,4,5,6]
pattern = [1,1]
ans = Solution().countMatchingSubarrays(nums, pattern)
print(ans)

nums = [1,4,4,1,3,5,5,3]
pattern = [1,0,-1]
ans = Solution().countMatchingSubarrays(nums, pattern)
print(ans)
