'''
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

# from collections import Counter, defaultdict

# import maths functions & constants
# from math import gcd
# from cmath import inf

# import functools.
# from functools import reduce

# import Generic Type
from typing import List


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        lw1 = lw2 = float('-inf')
        ans = float('inf')
        for idx, word in enumerate(wordsDict):
            if word == word1:
                ans = min(ans, idx-lw2)
                lw1 = idx
            elif word == word2:
                ans = min(ans, idx-lw1)
                lw2 = idx
        return ans
