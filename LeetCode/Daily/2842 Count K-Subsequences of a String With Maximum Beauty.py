"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

from collections import Counter
from math import comb


class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        counter = Counter(s)
        if k > len(counter):
            return 0
        freq_cnt = Counter([v for v in counter.values()])
        MOD = 10**9+7
        ans = 1
        steps = 0
        for key, val in sorted(freq_cnt.items(), reverse=True):
            if steps + val < k:
                ans = (ans * pow(key, val, MOD)) % MOD
            else:
                # length of string id being k now.
                c = comb(val, k-steps)
                ans = (ans*pow(key, k-steps, MOD)*c) % MOD
                break
            steps += val
        return ans
