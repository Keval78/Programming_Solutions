'''
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

# import maths functions & constants
# from math import gcd
# from cmath import inf

# import functools.
# from functools import reduce

from collections import defaultdict
from typing import List


class WordDistance:
    def __init__(self, wordsDict: List[str]):
        self.locations = defaultdict(list)
        for i, w in enumerate(wordsDict):
            self.locations[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        loc1, loc2 = self.locations[word1], self.locations[word2]
        i = j = 0
        min_diff = float("inf")
        while i < len(loc1) and j < len(loc2):
            min_diff = min(min_diff, abs(loc1[i] - loc2[j]))
            if loc1[i] < loc2[j]:
                i += 1
            else:
                j += 1
        return min_diff
