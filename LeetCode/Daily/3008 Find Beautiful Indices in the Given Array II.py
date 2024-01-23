'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List
from bisect import bisect_left, bisect

def knuth_morris_pratt(pattern: str, text: str) -> List[int]:
    """
    The Knuth-Morris-Pratt Algorithm for finding a pattern within a piece of text
    with complexity O(n + m)

    1) Preprocess pattern to identify any suffixes that are identical to prefixes

        This tells us where to continue from if we get a mismatch between a character
        in our pattern and the text.

    2) Step through the text one character at a time and compare it to a character in
        the pattern updating our location within the pattern if necessary
    """
    # 1) Construct the LPS array
    lps = get_lps_array(pattern)
    p_len = len(pattern)
    t_len = len(text)

    indices = []
    # 2) Step through text searching for pattern
    i, j = 0, 0  # index into text, pattern
    while i < t_len:
        if pattern[j] == text[i]:
            j += 1
        elif j > 0:
            j = lps[j - 1]
            continue
        
        if j == p_len:
            indices.append(i-p_len+1)
            j = lps[j - 1]
        
        i += 1
    return indices
    
def get_lps_array(pattern: str) -> List[int]:
    """
    Longest Prefix Suffix Array
    Calculates the new index we should go to if we fail a comparison
    """
    lps, prevLps, i = [0], 0, 1
    while i < len(pattern):
        if pattern[prevLps] == pattern[i]:
            prevLps += 1
        elif prevLps > 0:
            prevLps = lps[prevLps-1]
            continue
        i += 1
        lps.append(prevLps)
    return lps



class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n = len(s)

        a_indices = knuth_morris_pratt(a, s)
        b_indices = knuth_morris_pratt(b, s)
        
        indices = []
        for ind in a_indices:
            left = bisect_left(b_indices, ind-k)
            right = bisect(b_indices, ind+k)

            if right-left > 0:
                indices.append(ind)
        
        return indices



s = "isawsquirrelnearmysquirrelhouseohmy"
a = "my"
b = "squirrel"
k = 15
ans = Solution().beautifulIndices(s, a, b, k)
print(ans)

s = "abcd"
a = "a"
b = "a"
k = 4
ans = Solution().beautifulIndices(s, a, b, k)
print(ans)
