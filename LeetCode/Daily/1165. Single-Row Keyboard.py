"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""
from collections import defaultdict


class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        keys = [0]*26
        last_chr = keyboard[0]
        total_time = 0
        def key_ind(ch): return ord(ch)-ord('a')
        for i, ch in enumerate(keyboard):
            keys[key_ind(ch)] = i
        for ch in word:
            total_time += abs(keys[key_ind(ch)] - keys[key_ind(last_chr)])
            last_chr = ch
        return total_time
