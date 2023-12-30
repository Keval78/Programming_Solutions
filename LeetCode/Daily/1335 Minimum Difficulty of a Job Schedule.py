'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # self.minDifficulty_TopDownApproach(jobDifficulty, d)
        # self.minDifficulty_BottomUPApproach(jobDifficulty, d)
        return self.minDifficulty_BottomUPOptimize(jobDifficulty, d)

    def minDifficulty_TopDownApproach(self, jobDifficulty: List[int], d: int) -> int:
        INF = float('inf')
        n = len(jobDifficulty)
        # DP with memoization
        def topdowndp(idx, d):
            # print(idx)
            if d == 1:
                return max(jobDifficulty[idx:])
            
            if memo[idx][d] != -1: return memo[idx][d]
            
            curr_max, res = 0, INF
            for i in range(idx, n-d+1):
                curr_max = max(curr_max, jobDifficulty[i])
                res = min(res, curr_max + topdowndp(i+1, d-1))
            
            memo[idx][d] = res
            return res
        
        memo = [[-1]*(d+1) for i in range(n)]
        ans = topdowndp(0, d)
        # print(ans)
        return ans if ans != INF else -1

    def minDifficulty_BottomUPApproach(self, jobDifficulty: List[int], d: int) -> int:
        INF = float('inf')
        n = len(jobDifficulty)
        # DP with Tabular method.
        
        dp = [[INF]*(d+1) for i in range(n+1)]
        dp[n][0] = 0
        for remDays in range(1, d+1):
            for i in range(n-remDays+1):
                curr_max = 0
                for j in range(i, n-remDays+1):
                    curr_max = max(curr_max, jobDifficulty[j])
                    dp[i][remDays] = min(dp[i][remDays], curr_max + dp[j+1][remDays-1])
        ans = dp[0][d]
        return ans if ans != INF else -1

    def minDifficulty_BottomUPOptimize(self, jobDifficulty: List[int], d: int) -> int:
        INF = float('inf')
        n = len(jobDifficulty)
        # DP with Tabular method Space Complexity O(N).
        
        prevDp, currDp = [INF]*(n+1), [INF]*(n+1)
        prevDp[n] = 0
        
        for remDays in range(1, d+1):
            for i in range(n-remDays+1):
                curr_max = 0
                for j in range(i, n-remDays+1):
                    curr_max = max(curr_max, jobDifficulty[j])
                    currDp[i] = min(currDp[i], curr_max + prevDp[j+1])
            prevDp, currDp = currDp, [INF]*(n+1)
        ans = prevDp[0]
        return ans if ans != INF else -1

    def minDifficulty_MonotonicStack(self, jobDifficulty: List[int], d: int) -> int:
        # Monotonic Stack - Better Time Complexity
        pass
        return 0
    




jobDifficulty = [6,5,4,3,2,1]
d = 2
ans = Solution().minDifficulty(jobDifficulty, d)
print(ans)


jobDifficulty = [9,9,9]
d = 4
ans = Solution().minDifficulty(jobDifficulty, d)
print(ans)


jobDifficulty = [1,1,1]
d = 3
ans = Solution().minDifficulty(jobDifficulty, d)
print(ans)


