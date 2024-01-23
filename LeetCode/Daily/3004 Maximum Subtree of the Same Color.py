'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''

from collections import deque, defaultdict
from typing import List

class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        edge_map = defaultdict(list)
        for u, v in edges:
            edge_map[u].append(v)
            edge_map[v].append(u)
        
        def dfs(node, parent):
            nonlocal max_size
            if node != root and len(edge_map[node]) == 1: 
                return 1
            
            curr_size = 1
            mismatch = False
            for adj in edge_map[node]:
                if adj == parent: continue
                adj_size = dfs(adj, node)
                if colors[node] != colors[adj] or adj_size == 0:
                    mismatch = True
                else:
                    curr_size += adj_size
            
            if mismatch: return 0
            max_size = max(max_size, curr_size)
            return curr_size
                
        
        max_size = 1
        root = 0
        dfs(root, -1)
        return max_size

