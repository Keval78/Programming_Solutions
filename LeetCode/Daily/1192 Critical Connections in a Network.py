
from typing import List


class Solution:
    def dfs(self, node, parent, graph, tin, low, bridges):
        # Define intime and low
        self.timer += 1
        tin[node] = low[node] = self.timer

        for adj in graph[node]:
            if adj == parent:
                continue
            if tin[adj] == 0:
                self.dfs(adj, node, graph, tin, low, bridges)
                low[node] = min(low[node], low[adj])
                if low[adj] > tin[node]:
                    bridges.append([node, adj])
            else:
                low[node] = min(low[node], low[adj])

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # Tarjan's Algorithm
        graph = [[] for i in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        # Find Bridges for the graph
        self.timer = 0  # Create timer for each dfs call.
        bridges = []

        tin = [0]*n  # We use intime as visited if it is zero(0).
        low = [0]*n
        self.dfs(0, -1, graph, tin, low, bridges)

        return bridges
