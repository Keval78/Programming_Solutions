'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        n = len(words)
        cnt = 0
        for i in range(n):
            for j in range(i+1, n):
                m, l = len(words[i]), len(words[j])
                if l>=m and words[i] == words[j][:m] and words[i] == words[j][l-m:]:
                    cnt+=1

        return cnt