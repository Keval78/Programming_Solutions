"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n, m = len(s), s.count('1')
        return "1"*(m-1) + "0"*(n-m) + "1"
