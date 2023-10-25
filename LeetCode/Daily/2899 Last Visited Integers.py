'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from typing import List


class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        temp, idx, ans = [], 0, []
        for w in words:
            if w == "prev":
                idx -= 1
                ans.append(temp[idx] if abs(idx) <= len(temp) else -1)
            else:
                temp.append(int(w))
                idx = 0

        return ans
