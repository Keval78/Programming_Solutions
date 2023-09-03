"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""


from collections import defaultdict
from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:

        n = len(nums)
        pref = [0 for i in range(n+1)]
        for i in range(n):
            nums[i] = 1 if nums[i] % modulo == k else 0
            pref[i+1] = pref[i] + nums[i]
            pref[i+1] %= modulo

        cnt = defaultdict(int)
        dp = [0 for i in range(n+1)]
        for i in range(n+1):
            # dp[i] = last[pref[i+1]-k] #+ dp[pref[i+1]-k]
            dp[i] += cnt[(pref[i]-k) % modulo]
            cnt[pref[i]] += 1
            # print(cnt)

        # print(pref)
        # print(dp)
        # print(sum(dp))

        return sum(dp)
