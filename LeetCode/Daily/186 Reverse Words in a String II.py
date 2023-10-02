"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

from typing import List


class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        i, j = 0, 0
        while (i < n and j < n):
            while (j < n and s[j] != " "):
                j += 1
            k = j-1
            while (i < k):
                s[i], s[k] = s[k], s[i]
                i, k = i+1, k-1
            i, j = j+1, j+1
        i, j = 0, n-1
        while (i < j):
            s[i], s[j] = s[j], s[i]
            i, j = i+1, j-1
        return s
