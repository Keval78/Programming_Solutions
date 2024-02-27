'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from collections import Counter

class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        cntr = Counter(s)
        freq = max(cntr.values())
        
        indices = {}
        for idx, ch in enumerate(s):
            if cntr[ch] == freq:
                indices[ch] = idx
        
        ans = "".join([key for key in sorted(indices, key=indices.get)])
        return ans