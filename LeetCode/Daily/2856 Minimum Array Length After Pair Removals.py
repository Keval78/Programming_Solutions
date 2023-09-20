"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""


from typing import List


class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        ans = n % 2
        if len(freq) == 1:
            ans = freq[nums[0]]
        else:
            for num, val in freq.items():
                if val > n//2:
                    ans = val - (n - val)

        return ans
