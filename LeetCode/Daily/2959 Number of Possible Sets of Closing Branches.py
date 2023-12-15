'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List
from copy import deepcopy

class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        INF = float('inf')
        minDist = [[INF]*n for i in range(n)]
        
        for src in range(n):
            minDist[src][src] = 0
        
        for src, dest, cost in roads:
            minDist[src][dest] = min(minDist[src][dest], cost)
            minDist[dest][src] = minDist[src][dest]

        ans = 0
        for b in range(2**n):
            i = 0
            sets = []
            while b > 0:
                if b%2: sets.append(i)
                b //= 2
                i += 1
            # print(sets)

            setsDist = deepcopy(minDist)
            for k in sets:
                for src in sets:
                    for dest in sets:
                        setsDist[src][dest] = min(setsDist[src][dest], setsDist[src][k] + setsDist[k][dest])

            flag = True
            for src in sets:
                for dest in sets:
                    if setsDist[src][dest] > maxDistance:
                        flag = False
                        break
                if not flag: break
            
            if flag:
                ans += 1

        return ans


n = 3
maxDistance = 5
roads = [[0,1,2],[1,2,10],[0,2,10]]
ans = Solution().numberOfSets(n, maxDistance, roads)
print(ans)

n = 3
maxDistance = 5
roads = [[0,1,20],[0,1,10],[1,2,2],[0,2,2]]
ans = Solution().numberOfSets(n, maxDistance, roads)
print(ans)

n = 1
maxDistance = 10
roads = []
ans = Solution().numberOfSets(n, maxDistance, roads)
print(ans)
