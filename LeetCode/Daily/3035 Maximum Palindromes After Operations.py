'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List
from collections import defaultdict, Counter

class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        n, m = len(words), len(words[0])

        lens = [0] * n
        cntr = Counter()
        for i, word in enumerate(words):
            lens[i] = len(word)
            cntr += Counter(word)
        
        lens.sort()

        ans = 0
        ans1 = 0
        for l in lens:
            if l == 1:
                ans1 += 1
                # print("skipping length 1", l)
                continue
            
            if l % 2:
                for k in cntr:
                    if cntr[k] % 2:
                        l -= 1
                        cntr[k] -= 1
                        break
            
            if l % 2:
                for k in cntr:
                    if cntr[k] > 0:
                        l -= 1
                        cntr[k] -= 1
                        break


            need = l
            # print("need", need, cntr)
            for k in cntr:
                if cntr[k] > 1:
                    if cntr[k] < need:
                        need -= (cntr[k]//2)*2
                        cntr[k] = cntr[k]%2
                    else:
                        cntr[k] -= need
                        need = 0
            if need == 0:
                ans += 1

        return ans + ans1