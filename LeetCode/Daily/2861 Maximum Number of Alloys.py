'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List

class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        def isAlloyPossible(idx, unit):
            comp = composition[idx]
            c = 0
            for i in range(n):
                if stock[i] < (comp[i]*unit):
                    c += (comp[i]*unit - stock[i])*cost[i]
            # print(idx, unit, c)
            if c <= budget: return True
            else: return False
        

        ans = 0
        for i in range(k):
            ansi = 0
            l, r = 1, 10**9
            while l <= r:
                mid = (l+r)//2
                if isAlloyPossible(i, mid):
                    ansi = mid
                    l = mid+1
                else:
                    r = mid-1
            # print(i, ansi)
            ans = max(ans, ansi)
        return ans




n = 3
k = 2
budget = 15
composition = [[1,1,1],[1,1,10]]
stock = [0,0,0]
cost = [1,2,3]
ans = Solution().maxNumberOfAlloys(n, k, budget, composition, stock, cost)
print(ans)


n = 3
k = 2
budget = 15
composition = [[1,1,1],[1,1,10]]
stock = [0,0,100]
cost = [1,2,3]
ans = Solution().maxNumberOfAlloys(n, k, budget, composition, stock, cost)
print(ans)


n = 2
k = 3
budget = 10
composition = [[2,1],[1,2],[1,1]]
stock = [1,1]
cost = [5,5]
ans = Solution().maxNumberOfAlloys(n, k, budget, composition, stock, cost)
print(ans)

n = 4
k = 4
budget = 17
composition = [[10,10,1,5],[9,7,7,1],[6,3,5,9],[2,10,2,7]]
stock = [9,8,2,7]
cost = [9,2,6,10]
ans = Solution().maxNumberOfAlloys(n, k, budget, composition, stock, cost)
print(ans)


