'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List


class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        n = len(nums)
        if n == 2:
            return True
        pref = [0] + [nums[i] for i in range(n)]
        for i in range(n):
            pref[i+1] += pref[i]

        print(pref)
        dp = [[False for i in range(n)] for j in range(n)]

        for i in range(n):
            dp[i][i] = True

        for j in range(n-1):
            # print(j+i, pref[j+2] - pref[j])
            if pref[j+2] - pref[j] >= m:
                dp[j][j+1] = True

        for i in range(2, n):
            for j in range(n-i):
                dp[j][j+i] = dp[j][j+i-1] | dp[j+1][j+i]

        return dp[0][-1]
