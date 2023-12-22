'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from typing import List

class Solution:
    def countDivisibleSubstrings(self, word: str) -> int:
        keys = [1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9]
        
        n = len(word)
        val = [0]*(n+1)

        for i in range(n):
            val[i+1] += keys[ord(word[i]) - ord('a')] + val[i]

        ans = n
        for l in range(2, n+1):
            for j in range(l, n+1):
                if (val[j]-val[j-l])%l == 0:
                    ans += 1
        return ans



word = "asdf"
ans = Solution().countDivisibleSubstrings(word)
print(ans)

word = "bdh"
ans = Solution().countDivisibleSubstrings(word)
print(ans)

word = "abcd"
ans = Solution().countDivisibleSubstrings(word)
print(ans)

