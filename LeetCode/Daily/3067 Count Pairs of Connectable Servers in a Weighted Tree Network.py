'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from typing import List
from collections import defaultdict

class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        n = len(edges)+1
        edge_map = defaultdict(list)

        for s, t, w in edges:
            edge_map[s].append([t, w])
            edge_map[t].append([s, w])
        
        # print(edge_map)

        count = [0]*n

        def dfs(curr, parent, weight, nodes):
            if weight%signalSpeed==0:
                nodes[0] += 1
            
            for t, w in edge_map[curr]:
                if t == parent: continue
                dfs(t, curr, weight + w, nodes)
            
            return nodes

        mod_depths = defaultdict(list)
        for i in range(n):
            for t, w in edge_map[i]:
                nodes = [0]
                dfs(t, i, w, nodes)
                mod_depths[i].append(nodes[0])

        print(mod_depths)
        for i in range(n):
            m = len(mod_depths[i])
            s = sum(mod_depths[i])
            for j in range(m):
                count[i] += mod_depths[i][j] *(s - mod_depths[i][j])
            count[i] //= 2
        return count


edges = [[0,6,3],[6,5,3],[0,3,1],[3,2,7],[3,1,6],[3,4,2]]
signalSpeed = 3
ans = Solution().countPairsOfConnectableServers(edges, signalSpeed)
print(ans)

edges = [[0,1,1],[1,2,5],[2,3,13],[3,4,9],[4,5,2]]
signalSpeed = 1
ans = Solution().countPairsOfConnectableServers(edges, signalSpeed)
print(ans)