'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from heapq import heapify, heappop, heappush, heapreplace

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        cost = 0
        while len(sticks)>1:
            temp = heapq.heappop(sticks) + heapq.heappop(sticks)
            cost += temp
            heapq.heappush(sticks, temp)
        return cost
                
        


    