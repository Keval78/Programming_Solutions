"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""
from collections import defaultdict

def main():
    class Solution:
        def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
            n = len(nums1)
            value_ind = defaultdict()
            for i in range(n):
                value_ind[nums2[i]] = i
            
            mappings = [0]*n
            for i in range(n):
                mappings[i] = value_ind.get(nums1[i])
            return mappings


    Solution().anagramMappings()


if __name__ == "__main__":
    main()
