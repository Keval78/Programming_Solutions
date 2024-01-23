'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List
from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = Counter(word)
        i = ans = 0
        for key, val in sorted(cnt.items(), key=lambda x:-x[1]):
            ans += (i//8 + 1) * val
            i += 1
        
        return ans



word = "abcde"
ans = Solution().minimumPushes(word)
print(ans)

word = "xycdefghij"
ans = Solution().minimumPushes(word)
print(ans)
