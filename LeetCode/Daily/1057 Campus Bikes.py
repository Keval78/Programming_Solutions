'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from heapq import heapify, heappop, heappush, heapreplace

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        assigned = [False for i in range(len(bikes))]
        worker_rec = [-1 for i in range(len(workers))]

        def manhattan_distance(worker_loc, bike_loc):
            return abs(worker_loc[0] - bike_loc[0]) + abs(worker_loc[1] - bike_loc[1])
        
        worker_to_bike_list = []
        pq = []
        for worker, worker_loc in enumerate(workers):
            curr_worker_pairs = []
            for bike, bike_loc in enumerate(bikes):
                distance = manhattan_distance(worker_loc, bike_loc)
                curr_worker_pairs.append((distance, worker, bike))
            
            curr_worker_pairs.sort(reverse=True)
            heapq.heappush(pq, curr_worker_pairs.pop())
            worker_to_bike_list.append(curr_worker_pairs)
        
        while pq:
            distance, worker, bike = heapq.heappop(pq)
            if not assigned[bike]:
                assigned[bike] = True
                worker_rec[worker] = bike
            else:
                next_closest_bike = worker_to_bike_list[worker].pop()
                heapq.heappush(pq, next_closest_bike)
        
        return worker_rec
                
        


    