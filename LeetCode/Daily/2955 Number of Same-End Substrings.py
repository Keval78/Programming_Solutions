'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from typing import List

class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        freq = [[0]*26]
        for i in range(n):
            idx = ord(s[i]) - ord('a')
            temp = freq[-1].copy()
            temp[idx] += 1
            freq.append(temp)
        
        ans = []
        for start, end in queries:
            val = [(x-y) for x, y in zip(freq[end+1], freq[start])]
            curr_ans = 0
            for v in val:
                curr_ans += v + (v*(v-1))//2
            ans.append(curr_ans)
        return ans


s = "abcaab"
queries = [[0,0],[1,4],[2,5],[0,5]]
ans = Solution().sameEndSubstringCount(s, queries)
print(ans)

s = "abcd"
queries = [[0,3]]
ans = Solution().sameEndSubstringCount(s, queries)
print(ans)

