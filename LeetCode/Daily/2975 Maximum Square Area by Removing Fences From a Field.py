'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def maximizeSquareArea2(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hPossible = set()
        hPossible.add(m-1)
        for i in range(len(hFences)):
            hPossible.add(hFences[i]-1)
            hPossible.add(m-hFences[i])
            for j in range(i):
                hPossible.add(abs(hFences[i]-hFences[j]))

        # ans = max. side of square.
        ans = 0        
        if n-1 in hPossible: ans = max(ans, n-1)
        for i in range(len(vFences)):
            if vFences[i]-1 in hPossible:
                ans = max(ans, vFences[i]-1)
            if n-vFences[i] in hPossible:
                ans = max(ans, n-vFences[i])
            
            for j in range(i):
                diff = abs(vFences[i]-vFences[j])
                if diff in hPossible:
                    ans = max(ans, diff)

        return (ans * ans) % (10**9+7) if ans != 0 else -1

    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences = hFences + [1, m]
        hPossible = {abs(hFences[i]-hFences[j]) for i in range(len(hFences)) for j in range(i)}

        vFences = vFences + [1, n]
        vPossible = {abs(vFences[i]-vFences[j]) for i in range(len(vFences)) for j in range(i)}

        ans = next((x for x in sorted(vPossible, reverse=True) if x in hPossible), -1)
        
        return (ans * ans) % (10**9+7) if ans != -1 else -1


m = 4
n = 3
hFences = [2,3]
vFences = [2]
ans = Solution().maximizeSquareArea(m, n, hFences, vFences)
print(ans)


m = 6
n = 7
hFences = [2]
vFences = [4]
ans = Solution().maximizeSquareArea(m, n, hFences, vFences)
print(ans)
