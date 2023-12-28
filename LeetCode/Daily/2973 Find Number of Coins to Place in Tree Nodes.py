

'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List
from collections import defaultdict
from heapq import heapify, heappush, heappop


class Solution:
    def placedCoins2(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        n = len(cost)
        edge_map = defaultdict(list)
        for u, v in edges:
            edge_map[u].append(v)
            edge_map[v].append(u)

        coins = [0]*n
        node_cost = [[0]*5 for i in range(n)]
        
        def dfs_cost(node, parent):
            if parent!=-1 and len(edge_map[node]) == 1:
                # it is chils node:
                coins[node] = 1
                node_cost[node][0] = cost[node]
                return
            
            temp_cost = [cost[node]]
            for child in edge_map[node]:
                if child == parent: continue
                dfs_cost(child, node)
                temp_cost += node_cost[child]
            temp_cost.sort()
            node_cost[node] = temp_cost[:3] + temp_cost[-3:]
            # print(node, node_cost[node], temp_cost)
            if node_cost[node].count(0) > 3:
                coins[node] = 1
            else:
                coins[node] = max(0, temp_cost[0]*temp_cost[1]*temp_cost[-1],
                            temp_cost[-3]*temp_cost[-2]*temp_cost[-1])

        dfs_cost(0, -1)
        return coins

    
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        """Solution using Heap."""
        n = len(cost)
        edge_map = defaultdict(list)
        for u, v in edges:
            edge_map[u].append(v)
            edge_map[v].append(u)

        coins = [0]*n
        node_cost = [[0]*5 for i in range(n)]
        
        def dfs_cost(node, parent):
            if parent!=-1 and len(edge_map[node]) == 1:
                # it is chils node:
                coins[node] = 1
                node_cost[node][0] = cost[node]
                return
            
            neg, pos = [], []
            heapify(neg)
            heapify(pos)
            if cost[node] > 0:
                heappush(pos, cost[node])
            else:
                heappush(neg, abs(cost[node]))

            for child in edge_map[node]:
                if child == parent: continue
                dfs_cost(child, node)
                for c in node_cost[child]:
                    if c == 0: continue
                    if c > 0:
                        heappush(pos, c)
                        if len(pos) == 4: heappop(pos)
                    else:
                        heappush(neg, abs(c))
                        if len(neg) == 4: heappop(neg)

            node_cost[node] = sorted(pos + [-i for i in neg])
            # print(node, node_cost[node])
            if len(node_cost[node]) < 3:
                coins[node] = 1
            else:
                coins[node] = max(0, node_cost[node][0]*node_cost[node][1]*node_cost[node][-1], node_cost[node][-3]*node_cost[node][-2]*node_cost[node][-1])

        dfs_cost(0, -1)
        return coins
        


edges = [[0,1],[0,2],[0,3],[0,4],[0,5]]
cost = [1,2,3,4,5,6]
ans = Solution().placedCoins(edges, cost)
print(ans)


edges = [[0,1],[0,2],[1,3],[1,4],[1,5],[2,6],[2,7],[2,8]]
cost = [1,4,2,3,5,7,8,-4,2]
ans = Solution().placedCoins(edges, cost)
print(ans)

edges = [[0,1],[0,2]]
cost = [1,2,-2]
ans = Solution().placedCoins(edges, cost)
print(ans)

edges = [[0,1]]
cost = [1, 2]
ans = Solution().placedCoins(edges, cost)
print(ans)

edges = [[0,8],[8,1],[9,2],[4,6],[7,4],[3,7],[3,8],[5,8],[5,9]]
cost = [-4,83,-97,40,86,-85,-6,-84,-16,-53]
# [709070,1,1,43344,1,0,1,43344,709070,1]
ans = Solution().placedCoins(edges, cost)
print(ans)


