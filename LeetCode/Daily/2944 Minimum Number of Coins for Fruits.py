'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from typing import List

class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        # DP with memoization
        def topdowndp(idx, prevBought):
            if idx == n:
                return 0

            if memo[idx][prevBought] != -1:
                return memo[idx][prevBought]

            take = topdowndp(idx+1, min(2*idx+2, n)) + prices[idx]
            nontake = float('inf')
            if prevBought > idx:
                nontake = topdowndp(idx+1, prevBought)
            
            res = min(take, nontake)
            
            memo[idx][prevBought] = res
            return res

        memo = [[-1]*(n+1) for i in range(n)]
        ans = topdowndp(0, 0)
        return ans