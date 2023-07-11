'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from heapq import heapify, heappop, heappush, heapreplace
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        maps = [None for i in range(1001)]
        for item in items:
            _id, rank = item
            if maps[_id] is None:
                maps[_id] = [rank]
            else: maps[_id].append(rank)
        scores = []
        for i in range(1001):
            if maps[i] is not None:
                scores.append([i, sum(heapq.nlargest(5, maps[i]))//5])
        return scores
                
        


    