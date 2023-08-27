"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

from typing import List


class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers.sort(key=lambda x: x[0])
        # print(offers)

        def top_down_dp(idx, offers, memo):
            # print(idx)
            if idx >= len(offers):
                return 0

            if memo[idx] != -1:
                return memo[idx]

            l, r = idx+1, len(offers)-1
            while l <= r:
                mid = (l+r)//2
                if offers[mid][0] > offers[idx][1]:
                    r = mid - 1
                else:
                    l = mid + 1
            nex_idx = l
            # print(idx, nex_idx)

            res = max(offers[idx][2] + top_down_dp(nex_idx,
                      offers, memo), top_down_dp(idx+1, offers, memo))

            memo[idx] = res
            return res

        memo = [-1 for i in range(len(offers))]
        ans = top_down_dp(0, offers, memo)
        return ans
