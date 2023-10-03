"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        maps = [0]*26
        def stoi(ch): return ord(ch) - ord('a')
        for i in range(len(s)):
            maps[stoi(s[i])] += 1
        count = 0
        for num in maps:
            count += num % 2
        return count <= 1
