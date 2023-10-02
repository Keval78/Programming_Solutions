'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List
from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dp = [0]*(10**4+1)
        count = Counter(nums)

        for num, cnt in count.items():
            dp[num] = num*cnt

        dp[1] = max(dp[0], dp[1])
        for i in range(2, len(dp)):
            dp[i] = max(dp[i-1], dp[i] + dp[i-2])

        return dp[-1]
