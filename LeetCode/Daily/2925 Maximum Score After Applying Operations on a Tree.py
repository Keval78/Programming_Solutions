'''
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
'''
from typing import List
from collections import defaultdict

class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        edge_map = defaultdict(list)
        for u, v in edges:
            edge_map[u].append(v)
            edge_map[v].append(u)
        
        # print(edge_map)
        # DP with memoization
        def topdowndp(node, choose, parent, memo):
            if edge_map[node] == [parent]:
                if choose == 0:
                    return 0
                else:
                    return values[node]

            if memo[node][choose] != -1:
                return memo[node][choose]

            profit = 0
            if choose == 0:
                # way1: do not choose current node
                for adj in edge_map[node]:
                    if adj == parent: continue
                    profit += topdowndp(adj, 1, node, memo)
            
            # way2: choose current node and add into profit keep choose = 0 (same).
            profit2 = values[node]
            for adj in edge_map[node]:
                if adj == parent: continue
                profit2 += topdowndp(adj, choose, node, memo)
            
            res = max(profit, profit2)

            memo[node][choose] = res
            return res

        memo = [[-1]*2 for i in range(len(values))]
        ans = topdowndp(0, 0, -1, memo)
        return ans


# edges = [[0,1],[0,2],[0,3],[2,4],[4,5]]
# values = [5,2,5,2,1,1]
# ans = Solution().maximumScoreAfterOperations(edges, values)
# print(ans)


# edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
# values = [20,10,9,7,4,3,5]
# ans = Solution().maximumScoreAfterOperations(edges, values)
# print(ans)


edges = [[7,0],[3,1],[6,2],[4,3],[4,5],[4,6],[4,7]]
values = [2,16,23,17,22,21,8,6]
ans = Solution().maximumScoreAfterOperations(edges, values)
print(ans)