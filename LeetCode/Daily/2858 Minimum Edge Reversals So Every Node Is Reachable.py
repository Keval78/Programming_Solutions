"""
###### * User Profile : Keval_78 
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""
from collections import defaultdict
from typing import List


class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        # * TWO WAYS * #
        '''Solution 1:
        1. Cosider any node as root node. count the total cost or edges which needs to reverse for the root node.
        2. Total cost = Number of edges needs to reverse for root.
        3. Use DFS to count cost to reach the node and depth of the node.
        4. Cost(node) = Cost(root) + cost_to_reach_root - cost_of_path_from_node_to_root
                      = Total_cost - (depth - #_reverse_node_in_path) - #_reverse_node_in_path
        '''

        # graph with the forward edges which incurred cost 0.
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append((v, 0))
            graph[v].append((u, 1))

        # print(graph)

        # consider Node = 0 as start node.
        def dfs(node, parent, depth, cost):
            """DFS to count depth and cost of node.
            """
            # count depth
            costs[node] = depth - 2*cost

            nonlocal total_cost
            for adj, c in graph[node]:
                if adj == parent:
                    total_cost += 1 - c
                    continue
                dfs(adj, node, depth+1, cost+c)

        total_cost = 0
        costs = [0]*n
        dfs(0, -1, 0, 0)
        for i in range(n):
            costs[i] += total_cost

        return costs

    def minEdgeReversals2(self, n: int, edges: List[List[int]]) -> List[int]:
        '''Solution 2: In-Out DP
        1. Cosider any node as root node. count the total cost or edges which needs to reverse for the root node.
        2. Total cost = Number of edges needs to reverse for root.
        3. For child node Cost = Cost(child_subtree) + Cost(parent_subtree_without_current_child) + cost_of_edge
        '''
        # Solution 2
        cost_down = [0]*n
        cost_up = [0]*n
        # graph with the forward edges which incurred cost 0.
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append((v, 0))
            graph[v].append((u, 1))

        # Find the cost of each subtree.
        def dfs_cost_subtree(node, parent, cost_down):
            for adj, c in graph[node]:
                if adj == parent:
                    continue
                dfs_cost_subtree(adj, node, cost_down)
                cost_down[node] += cost_down[adj] + c
        dfs_cost_subtree(0, -1, cost_down)
        # print(cost_down)

        # Find the cost of each parent without current subtree.
        def dfs_cost_parent(node, parent, cost_up):
            for adj, c in graph[node]:
                if adj == parent:
                    continue
                # Cost of parent without current child
                cost_up[adj] = cost_down[node] - cost_down[adj] - c
                # Cost of edge
                cost_up[adj] += (1-c)
                # add cost up of parent because grandparent will be child of parent.
                # if we consider adj node as root.
                cost_up[adj] += cost_up[node]

                dfs_cost_parent(adj, node, cost_up)

        dfs_cost_parent(0, -1, cost_up)
        # print(cost_up)

        return [i+j for i, j in zip(cost_down, cost_up)]
