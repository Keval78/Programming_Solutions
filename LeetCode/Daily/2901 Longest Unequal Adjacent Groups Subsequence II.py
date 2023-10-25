'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from typing import List


class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        dp = [(1, -1)]*n
        def hamd(x, y): return sum(1 for i, j in zip(x, y) if i != j)
        idx, max_len = -1, 0
        for i in range(n):
            for j in range(i-1, -1, -1):
                if groups[i] != groups[j] and len(words[i]) == len(words[j]) and hamd(words[i], words[j]) == 1:
                    if dp[i][0] < dp[j][0] + 1:
                        dp[i] = (dp[j][0] + 1, j)
            # print(dp)
            if dp[i][0] > max_len:
                max_len = dp[i][0]
                idx = i

        # print(idx)
        ans = [None]*max_len
        ans[-1] = words[idx]

        j = -2
        while dp[idx][1] != -1:
            ans[j] = words[dp[idx][1]]
            idx = dp[idx][1]
            j -= 1

        return ans
