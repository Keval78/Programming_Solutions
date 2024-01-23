'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        dist = [[0]*n for i in range(n)]

        for i in range(n):
            for j in range(n):
                dist[i][j] = abs(i-j)        

        if x != y:
            dist[x-1][y-1] = 1
            dist[y-1][x-1] = 1

        # Do relaxations for each vertex.
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        ans = [0 for i in range(n)]
        for i in range(n):
            for j in range(n):
                if dist[i][j] !=0:
                    ans[dist[i][j]-1] += 1
        

        return ans




n = 3
x = 1
y = 3
ans = Solution().countOfPairs(n, x, y)
print(ans)

n = 5
x = 2
y = 4
ans = Solution().countOfPairs(n, x, y)
print(ans)

n = 4
x = 1
y = 1
ans = Solution().countOfPairs(n, x, y)
print(ans)