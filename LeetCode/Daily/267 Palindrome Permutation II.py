"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

from typing import List
from collections import Counter
from itertools import permutations


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        res = []

        # Check string can be arranged as palindrome.
        freq = Counter(s)
        odd_cnt, odd_char = 0, ''
        chars = []
        for k, v in freq.items():
            if v % 2:
                odd_cnt += 1
                odd_char = k
            else:
                chars += [k]*(v//2)
        if odd_cnt > 1:
            return res

        # recursively generate all the permutations of each key of chars.
        # print(chars)

        # for p in itertools.permutations(chars):
        #     res.append(''.join(p)  + odd_char + ''.join(p[::-1]))

        def permutation(start, chars, res):
            if len(chars) == 0 or start == len(chars)-1:
                res.append(''.join(chars) + odd_char + ''.join(chars[::-1]))
                return

            for i in range(start, len(chars)):
                if chars[i] in chars[start:i]:
                    continue
                chars[start], chars[i] = chars[i], chars[start]
                permutation(start+1, chars, res)
                chars[i], chars[start] = chars[start], chars[i]
        chars.sort()
        # print(chars)
        permutation(0, chars, res)
        # print(len(res))
        return res
