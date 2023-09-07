'''
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7

        # DP with Moemoization.
        def digitdp(idx: int, tight1: int, tight2: int, rsum: int, num1: str, num2: str):
            #print(idx, tight1, tight2, rsum, num1, num2)
            if rsum < 0: return 0
            if idx == len(num2): return 1
            
            if memo[idx][tight1][tight2][rsum] != -1:
                return memo[idx][tight1][tight2][rsum]

            lo = ord(num1[idx]) - ord('0') if tight1 else 0
            hi = ord(num2[idx]) - ord('0') if tight2 else 9
            #print(lo, hi)
            res = 0
            for i in range(lo, hi+1):
                res += digitdp(idx+1, tight1 & (i == lo), tight2 & (i == hi), rsum-i, num1, num2)
                res %= MOD

            memo[idx][tight1][tight2][rsum] = res
            return res

        num1 = '0'*(len(num2) - len(num1)) + num1

        memo = [[[[-1]*(max_sum+1) for i in range(2)] for j in range(2)] for k in range(23)]
        ans1 = digitdp(0, 1, 1, max_sum, num1, num2)

        memo = [[[[-1]*(min_sum) for i in range(2)] for j in range(2)] for k in range(23)]
        ans2 = digitdp(0, 1, 1, min_sum-1, num1, num2)
        #print(ans1, ans2)
        return (ans1 - ans2)%MOD
        