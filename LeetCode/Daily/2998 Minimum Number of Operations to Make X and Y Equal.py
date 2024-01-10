'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from collections import deque


class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        if y >= x: return y-x
        
        visited = [False for i in range(10**5)]
        que = deque([(x, 0)])

        while que:
            # print(que)
            
            num, cost = que.popleft()

            if num == y: return cost
            if num == 0: continue

            if not visited[num+1]:
                que.append((num+1, cost+1))
                visited[num+1] = True
            
            if not visited[num-1]:
                que.append((num-1, cost+1))
                visited[num-1] = True

            if not visited[num//5] and num % 5 == 0:
                que.append((num//5, cost+1))
                visited[num//5] = True
            if not visited[num//11] and num % 11 == 0:
                que.append((num//11, cost+1))
                visited[num//11] = True

        return -1
            
        
        

x = 26
y = 1
ans = Solution().minimumOperationsToMakeEqual(x, y)
print(ans)

x = 54
y = 2
ans = Solution().minimumOperationsToMakeEqual(x, y)
print(ans)

x = 25
y = 30
ans = Solution().minimumOperationsToMakeEqual(x, y)
print(ans)