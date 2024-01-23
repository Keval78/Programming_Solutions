'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        if x>y: x, y = y, x
        
        dist = [0]*(n+2)
        if x==y or x+1==y:
            for i in range(1, n):
                dist[1] += 1
                dist[n-i+1] -= 1
            result = [0]*n
            for i in range(1, n+1):
                dist[i] += dist[i-1]
                result[i-1] = dist[i]*2
            return result

        mid = y-(y-x)//2
        for i in range(mid, n+1):
            dist[1] += 1
            dist[n-i+1] -= 1
        
        for i in range(1, x):
            # i...mid
            dist[1] += 1
            dist[mid-i+1] -= 1

            # mid+1...i-1
            if (mid+1 <= y-1):
                dist[x-i+2] += 1
                dist[x-i+1+y-mid] -= 1

            # y...n
            dist[x-i+1] += 1
            dist[x-i+n-y+2] -= 1


        for i in range(x, mid):
            to = mid + (i - x)
            
            # i...to
            dist[1] += 1
            dist[to-i+1] -= 1            

            # i...to
            if (to+1 <= y):
                dist[i-x+1] += 1
                dist[i-x+y-to+1] -= 1

            # y+1...n
            if (to+1 <= n):
                dist[i-x+2] += 1
                dist[i-x+n-y+2] -= 1

        result = [0]*n
        for i in range(1, n+1):
            dist[i] += dist[i-1]
            result[i-1] = dist[i]*2
        return result


n = 13
x = 11
y = 13
ans = Solution().countOfPairs(n, x, y)
print(ans)

# n = 13
# x = 3
# y = 9
# ans = Solution().countOfPairs(n, x, y)
# print(ans)

# n = 3
# x = 1
# y = 3
# ans = Solution().countOfPairs(n, x, y)
# print(ans)

# n = 5
# x = 2
# y = 4
# ans = Solution().countOfPairs(n, x, y)
# print(ans)

# n = 4
# x = 1
# y = 1
# ans = Solution().countOfPairs(n, x, y)
# print(ans)