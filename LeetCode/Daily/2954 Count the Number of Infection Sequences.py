'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from functools import cache
from typing import List

class Solution:
    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        """
        Approach: Star & Bars Pattern
        """
        @cache
        def ncrmod(n, r, mod):
            num = den = 1
            for i in range(r):
                num = (num * (n - i)) % mod
                den = (den * (i + 1)) % mod
            return (num * pow(den, mod - 2, mod)) % mod


        MOD = 10**9+7
        ans = 1
        for i in range(1, len(sick)):
            m = sick[i]-sick[i-1]-1
            ans *= (pow(2, max(0,m-1), MOD) * ncrmod(sick[i]-i, m, MOD)) % MOD
            ans %= MOD

        ans = (ans * ncrmod(n-len(sick), n-sick[-1]-1, MOD)) % MOD
        return ans


n = 5
sick = [0,4]
ans = Solution().numberOfSequence(n, sick)
print(ans)

n = 4
sick = [1]
ans = Solution().numberOfSequence(n, sick)
print(ans)

n = 5
sick = [2]
ans = Solution().numberOfSequence(n, sick)
print(ans)

n = 5
sick = [0,1]
ans = Solution().numberOfSequence(n, sick)
print(ans)

n = 5
sick = [0,4]
ans = Solution().numberOfSequence(n, sick)
print(ans)

n = 5
sick = [1,2]
ans = Solution().numberOfSequence(n, sick)
print(ans)

n = 101
sick = [40,48,56,83,90]
ans = Solution().numberOfSequence(n, sick)
print(ans)

n = 100000
sick = [5088,5735,9388,11485,24964,29671,32648,32960,35190,36621,37919,42363,48615,49156,55917,58071,59875,63578,65430,69035,74889,78641,78896,79290,83289,83869,84405,99339]
ans = Solution().numberOfSequence(n, sick)
print(ans)