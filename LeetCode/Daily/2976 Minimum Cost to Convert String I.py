'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        # Preprocessing using Floyd Warshall.
        INF = float('inf')
        mincost = [[INF]*26 for i in range(26)]

        n = len(original)
        for i in range(n):
            s = ord(original[i]) - ord('a')
            t = ord(changed[i]) - ord('a')
            c = cost[i]
            mincost[s][t] = min(mincost[s][t], c)
        
        # Do relaxation of all the vertices.
        for k in range(26):
            for s in range(26):
                for t in range(26):
                    if s==t: mincost[s][t] = 0
                    else: mincost[s][t] = min(mincost[s][t], mincost[s][k] + mincost[k][t])
        
        ans = 0
        for x, y in zip(source, target):
            s, t = ord(x) - ord('a'), ord(y) - ord('a')
            # print(s,"->",t,"=",mincost[s][t])
            ans += mincost[s][t]
        
        return ans if ans != INF else -1



source = "abcd"
target = "acbe"
original = ["a","b","c","c","e","d"]
changed = ["b","c","b","e","b","e"]
cost = [2,5,5,1,2,20]
ans = Solution().minimumCost(source, target, original, changed, cost)
print(ans)


source = "aaaa"
target = "bbbb"
original = ["a","c"]
changed = ["c","b"]
cost = [1,2]
ans = Solution().minimumCost(source, target, original, changed, cost)
print(ans)

source = "abcd"
target = "abce"
original = ["a"]
changed = ["e"]
cost = [10000]
ans = Solution().minimumCost(source, target, original, changed, cost)
print(ans)
