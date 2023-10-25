'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from typing import List


class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        flag0, flag1 = 0, 1
        ans0, ans1 = [], []
        for i, (w, g) in enumerate(zip(words, groups)):
            if flag0 == g:
                ans0.append(w)
                flag0 = 1-flag0
            if flag1 == g:
                ans1.append(w)
                flag1 = 1-flag1
        return ans0 if len(ans0) > len(ans1) else ans1
