"""
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/
"""

from __future__ import annotations
from collections import defaultdict


def dfs(node, visited, graph, tp_sorting):
    """DFS for the graph"""
    visited[node] = True
    for adj in graph[node].values():
        if not visited[adj]:
            dfs(adj, visited, graph, tp_sorting)
    tp_sorting.append(node)


def kosaraju(graph):
    """A linear time algorithm to find the strongly connected components of a directed graph."""

    # Step 1: DFS traversal to define the priorities of the vertices -> Topo sort.
    n = len(graph)
    visited = [False] * n
    tp_sorting = []

    for node in graph:
        if not visited[node]:
            dfs(node, visited, graph, tp_sorting)
    # print(tp_sorting)

    # Step 2: Build the transpose graph.
    reversed_graph = defaultdict(list)
    for node in graph:
        for adj in graph[node]:
            reversed_graph[adj].append(node)

    # Step 3: DFS traversal on TG & Count components.
    visited = [False] * n
    components = []
    while tp_sorting:
        node = tp_sorting.pop()
        if not visited[node]:
            component = []
            dfs(node, visited, reversed_graph, component)
            components.append(component)
    # print(components)


if __name__ == "__main__":
    # Adjacency List of Graph
    graph = {0: [1, 2], 1: [3], 2: [3], 3: [4, 5], 4: [], 5: []}
    # Topological Sort (Graph)
    kosaraju(graph)
