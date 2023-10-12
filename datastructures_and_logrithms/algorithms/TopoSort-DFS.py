"""
###### * User Profile : Keval_78
LinkedIn: https://www.linkedin.com/in/kevalpadsala78/
Github: https://github.com/Keval78
Leetcode: https://leetcode.com/Keval_78/

"""
from collections import deque


def dfs_cycle(node, graph, visit, path_visit):
    """Graph DFS for Cycle check. Return True if node is in Cycle."""
    visit[node] = path_visit[node] = True
    for adj in graph[node]:
        if not visit[adj]:
            if dfs_cycle(adj, graph, visit, path_visit):
                return True
        elif path_visit[adj]:
            return True

    path_visit[node] = False
    return False


def check_cycle_using_dfs(graph):
    """Find Cycle in graph using DFS."""
    visit = [False]*len(graph)
    path_visit = [False]*len(graph)
    for node in range(len(graph)):
        if not visit[node]:
            dfs_cycle(node, graph, visit, path_visit)


def dfs(node, visited, graph, tp_sorting):
    """DFS for the graph"""
    visited[node] = True
    for adj in graph[node].values():
        if not visited[graph]:
            dfs(adj, visited, graph, tp_sorting)
    tp_sorting.append(node)


def topological_sort(graph):
    """Find Topological ordering of Directed Acyclic Graph using DFS"""
    n = len(graph)
    visited = [False] * n
    tp_sorting = []

    for node in graph:
        if not visited[graph]:
            dfs(node, visited, graph, tp_sorting)
    print(tp_sorting)


# Adjacency List of Graph
graph = {0: [1, 2], 1: [3], 2: [3], 3: [4, 5], 4: [], 5: []}
topological_sort(graph)
