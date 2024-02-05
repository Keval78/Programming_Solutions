'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List
from heapq import heapify, heappop, heappush
from bisect import bisect_left
from sortedcontainers import SortedList



class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        n = len(arrival)
        requests = [0] * k
        heap, free = [], SortedList(list(range(k)))

        for i in range(n):
            
            while heap and heap[0][0] <= arrival[i]:
                _, server = heappop(heap)
                free.add(server)

            if free:
                server = free[free.bisect_left(i%k)%len(free)]
                free.remove(server)
                heappush(heap, (arrival[i] + load[i], server))
                requests[server] += 1

            else:
                #skip th request server not available.
                pass
        
        max_requests = max(requests)
        return [i for i, r in enumerate(requests) if r==max_requests]

    
    def busiestServers2(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        requests = [0] * k
        heap, free = [], list(range(k))

        for i, start in enumerate(arrival):
            print(heap, free)

            while heap and heap[0][0] <= start:
                _, server_id = heappop(heap)
                heappush(free, i + (server_id - i) % k)

            # Get the original server ID by taking the remainder of
            # the modified ID to k.
            if free:
                busy_id = heappop(free) % k
                heappush(heap, (start + load[i], busy_id))
                requests[busy_id] += 1
        
        max_requests = max(requests)
        return [i for i, r in enumerate(requests) if r==max_requests]


k = 3
arrival = [1,2,3,4,5]
load = [5,2,3,3,3]
ans = Solution().busiestServers(k, arrival, load)
print(ans)

k = 3
arrival = [1,2,3,4]
load = [1,2,1,2]
ans = Solution().busiestServers(k, arrival, load)
print(ans)

k = 3
arrival = [1,2,3]
load = [10,12,11]
ans = Solution().busiestServers(k, arrival, load)
print(ans)

