'''
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        MOD = 10**9 + 7

        # DP with Memoization
        def digitdp(idx: int, prev: int, leading: int, tight1: int, tight2: int, low: str, high: str, memo):
            #print(idx, prev, leading, tight1, tight2, low, high)
            
            if idx == len(high):
                return 1
            
            if memo[idx][prev][leading][tight1][tight2] != -1:
                return memo[idx][prev][leading][tight1][tight2]

            res = 0
            lo = int(low[idx]) if tight1 else 0
            hi = int(high[idx]) if tight2 else 9
            for i in range(lo, hi+1):
                if not leading and abs(prev-i) != 1: continue
                res += digitdp(idx+1, i, leading & (i==0), tight1 & (i == int(low[idx])), tight2 & (i == int(high[idx])), low, high, memo)
                res %= MOD

            #print(idx, "->", res)
            memo[idx][prev][leading][tight1][tight2] = res
            return res

        memo = [[[[[-1]*(2) for i in range(2)] for j in range(2)] for l in range(10)] for k in range(101)]
        low = '0'*(len(high) - len(low)) + low
        ans = digitdp(0, 0, 1, 1, 1, low, high, memo)
        return ans